from __future__ import division, absolute_import, print_function, unicode_literals
from time import sleep, time
from threading import Event
import logging

import RPi.GPIO as GPIO
import spidev

from .configuration import IRQFlags1, IRQFlags2, OpMode, Temperature1, RSSIConfig
from .constants import Register, RF


class RadioError(Exception):
    pass


def wait_for(condition, timeout=5, check_time=0.005):
    """ Wait for a radio condition to become true within a timeout.
        If this doesn't happen, raise a RadioError.

        Returns the amount of time """
    start = time()
    iter_count = 0
    while not condition():
        # We're spinning quite fast here, so only get the current time
        # every 20 iterations
        if iter_count % 20 == 0 and (time() - start) > timeout:
            raise RadioError("Condition didn't become true within %s seconds" % timeout)
        sleep(check_time)
        iter_count += 1
    return time() - start


class RFM69(object):
    """ Interface for the RFM69 series of radio modules. """
    def __init__(self, reset_pin=None, dio0_pin=None, spi_channel=None, config=None):
        """ Initialise the object and configure the receiver.

            reset_pin -- the GPIO pin number which is attached to the reset pin of the RFM69
            dio0_pin  -- the GPIO pin number which is attached to the DIO0 pin of the RFM69
            spi_channel -- the SPI channel used by the RFM69
            config    -- an instance of `RFM69Configuration`
        """
        self.log = logging.getLogger(__name__)
        self.reset_pin = reset_pin
        self.dio0_pin = dio0_pin
        self.spi_channel = spi_channel
        self.config = config
        self.rx_restarts = 0
        self.init_gpio()
        self.init_spi()
        self.reset()
        self.write_config()
        self.log.info("Initialised successfully")

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dio0_pin, GPIO.IN)

    def init_spi(self):
        self.spi = spidev.SpiDev()
        self.spi.open(self.spi_channel, 0)
        self.spi.bits_per_word = 8
        self.spi.max_speed_hz = 50000

    def reset(self):
        """ Reset the module, then check it's working. """
        self.log.debug("Initialising RFM...")
        GPIO.setup(self.reset_pin, GPIO.OUT)
        GPIO.output(self.reset_pin, 1)
        sleep(0.05)
        GPIO.setup(self.reset_pin, GPIO.IN)
        sleep(0.05)
        if (self.spi_read(Register.VERSION) != 0x24):
            raise RadioError("Failed to initialise RFM69")

    def payload_ready_interrupt(self, pin):
        self.log.debug("Payload Ready Interrupt")
        self.packet_ready_event.set()

    def write_config(self):
        """ Write the full configuration to the module. This is called on
            initialisation.
        """
        self.log.debug("Writing configuration...")
        count = 0
        for register, value in self.config.get_registers().iteritems():
            self.spi_write(register, value)
            count += 1

        self.log.debug("%s configuration registers written.", count)

    def wait_for_packet(self, timeout=None):
        """ Put the module in receive mode, and block until we receive a packet.
            Returns a tuple of (packet, rssi), or None if there was a timeout

            timeout -- the amount of time to wait for before returning if no
                       packets were received.
        """
        start = time()
        self.packet_ready_event = Event()
        self.rx_restarts = 0
        GPIO.add_event_detect(self.dio0_pin, GPIO.RISING, callback=self.payload_ready_interrupt)
        self.set_mode(OpMode.RX)
        packet_received = False
        while True:
            irqflags = self.read_register(IRQFlags1)
            if not irqflags.mode_ready:
                self.log.error("Module out of ready state: %s", irqflags)
                break
            if irqflags.rx_ready and irqflags.timeout:
                # Once the RFM's receiver has been started by a signal over the RSSI
                # threshold, it will continue running (possibly with stale AGC/AFC
                # parameters). Detect this and reset the receiver.
                irqflags2 = self.read_register(IRQFlags2)
                self.log.debug("Restarting Rx on timeout. RSSI: %s, sync: %s, fifo_not_empty: %s, crc: %s",
                               irqflags.rssi, irqflags.sync_address_match, irqflags2.fifo_not_empty,
                               irqflags2.crc_ok)
                self.spi_write(Register.PACKETCONFIG2,
                               self.spi_read(Register.PACKETCONFIG2) | RF.PACKET2_RXRESTART)
                self.rx_restarts += 1
            if timeout is not None and time() - start > timeout:
                break
            if self.packet_ready_event.wait(1):
                packet_received = True
                break

        GPIO.remove_event_detect(self.dio0_pin)
        self.set_mode(OpMode.Standby, wait=False)

        if packet_received:
            rssi = self.get_rssi()
            data_length = self.spi_read(Register.FIFO)
            data = self.spi_burst_read(Register.FIFO, data_length)

            self.log.info("Received message: %s, RSSI: %s", data, rssi)
            return (bytearray(data), rssi)
        else:
            return None

    def send_packet(self, data, preamble=None):
        """ Transmit a packet. If you've configured the RFM to use variable-length
            packets, this function will add a length byte for you.

            The radio will be returned to the standby state.

            data -- this should be a bytearray. If it isn't, we'll try and convert it,
                    but you might end up with encoding issues, especially if you use
                    unicode strings.
            preamble -- how long, in seconds, to send the preamble bytes for. Longer
                    preambles may result in more reliable decoding, at the expense of
                    spectrum use.
        """
        data = bytearray(data)

        if self.config.packet_config_1.variable_length:
            data = [len(data)] + list(data)

        self.log.debug("Initialising Tx...")
        start = time()
        self.set_mode(OpMode.TX, wait=False)
        wait_for(lambda: self.read_register(IRQFlags1).tx_ready)

        self.log.debug("In Tx mode (took %.3fs)", time() - start)

        if preamble:
            sleep(preamble)

        self.write_fifo(data)
        wait_for(lambda: self.read_register(IRQFlags2).packet_sent)

        self.set_mode(OpMode.Standby)
        self.log.debug("Packet (%r) sent in %.3fs", data, time() - start)

    def set_mode(self, mode, wait=True):
        """ Change the mode of the radio. Mode values can be found in the OpMode class.

            wait -- wait for the mode_ready interrupt flag to be set before returning.
                    Not needed if you're going to be checking for another status flag.
        """
        start = time()
        self.config.opmode.mode = mode
        self.write_register(self.config.opmode)
        while wait:
            irqflags = self.read_register(IRQFlags1)
            if irqflags.mode_ready:
                duration = time() - start
                self.log.debug("Mode changed to %s in %.3fs", mode, duration)
                return
            sleep(0.005)
            if time() - start > 5:
                self.log.warn("Mode not set after 5 seconds, resetting module")
                self.reset()
                self.write_register(self.config.opmode)
                start = time()

    def get_rssi(self):
        """ Get the current RSSI in dBm. """
        return -(self.spi_read(Register.RSSIVALUE) / 2)

    def get_rssi_threshold(self):
        """ Get the current RSSI threshold in dBm. """
        return -(self.spi_read(Register.RSSITHRESH) / 2)

    def set_rssi_threshold(self, value):
        """ Set the RSSI threshold in dBm """
        if not -127 < value < 0:
            raise ValueError("RSSI threshold out of range")
        self.spi_write(Register.RSSITHRESH, -int(value * 2))

    def calibrate_rssi_threshold(self, samples=10):
        """ Try and estimate the local noise floor and set a good RSSI threshold. The RFM
            appears to work best when it has a good RSSI threshold set.

            We do this by taking n samples of the measured RSSI, 200ms apart, and discarding
            the highest (noisiest, most powerful) 80% of these.
        """
        old_thresh = self.spi_read(Register.RSSITHRESH)

        # Set the threshold to the lowest possible value and start receiving
        self.spi_write(Register.RSSITHRESH, 0xff)
        self.set_mode(OpMode.RX, wait=False)

        wait_for(lambda: self.read_register(RSSIConfig).rssi_done)

        values = []
        for i in range(0, samples):
            values.append(self.spi_read(Register.RSSIVALUE))
            sleep(0.2)

        values = sorted(values)
        new_thresh = values[int(samples * 0.8)] - 6

        self.set_mode(OpMode.Standby)

        if old_thresh != new_thresh:
            self.log.info("Changing RSSI threshold %sdB -> %sdB", -old_thresh / 2, -new_thresh / 2)
        self.spi_write(Register.RSSITHRESH, new_thresh)

    def read_temperature(self):
        """ Read the temperature from the RFM's built-in sensor.
            This will switch the module to standby mode.
        """
        self.set_mode(OpMode.Standby)
        reg = Temperature1()
        reg.start = True
        self.write_register(reg)
        wait_for(lambda: not self.read_register(Temperature1).running)

        return 168 - self.spi_read(Register.TEMP2)

    def read_register(self, register_cls):
        resp = self.spi_read(register_cls.REGISTER)
        return register_cls.unpack(resp)

    def write_register(self, register):
        self.spi_write(register.REGISTER, register.pack())

    def spi_read(self, register):
        data = [register & ~0x80, 0]
        resp = self.spi.xfer2(data)
        return resp[1]

    def spi_burst_read(self, register, length):
        data = [register & ~0x80] + ([0] * (length))
        # We get the length again as the first character of the buffer
        return self.spi.xfer2(data)[1:]

    def spi_write(self, register, value):
        data = [register | 0x80, value]
        self.spi.xfer2(data)

    def write_fifo(self, data):
        self.spi.xfer2([Register.FIFO | 0x80] + data)
