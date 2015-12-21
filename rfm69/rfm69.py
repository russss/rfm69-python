from __future__ import division, absolute_import, print_function, unicode_literals
from time import sleep, time
from threading import Event
import logging

import RPi.GPIO as GPIO
import spidev

from .configuration import IRQFlags1, IRQFlags2, OpMode, Temperature1
from .constants import Register


class RadioError(Exception):
    pass


class RFM69(object):
    def __init__(self, reset_pin=None, dio0_pin=None, dio4_pin=None, spi_channel=None, config=None):
        self.log = logging.getLogger(__name__)
        self.reset_pin = reset_pin
        self.dio0_pin = dio0_pin
        self.dio4_pin = dio4_pin
        self.spi_channel = spi_channel
        self.config = config
        self.init_gpio()
        self.init_spi()
        self.reset()
        self.write_config()
        self.log.info("Initialised successfully")

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dio0_pin, GPIO.IN)
        GPIO.setup(self.dio4_pin, GPIO.IN)

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
        self.log.debug("Writing configuration...")
        count = 0
        for register, value in self.config.get_registers().iteritems():
            self.spi_write(register, value)
            count += 1

        self.log.debug("%s configuration registers written.", count)

    def wait_for_packet(self, timeout=None):
        start = time()
        self.packet_ready_event = Event()
        GPIO.add_event_detect(self.dio0_pin, GPIO.RISING, callback=self.payload_ready_interrupt)
        self.set_mode(OpMode.RX)
        packet_received = False
        while True:
            irqflags = self.read_register(IRQFlags1)
            if not irqflags.mode_ready:
                self.log.error("Module out of ready state: %s", irqflags)
                break
            if timeout is not None and time() - start > timeout:
                break
            if self.packet_ready_event.wait(1):
                packet_received = True
                break

        GPIO.remove_event_detect(self.dio0_pin)
        self.set_mode(OpMode.Standby)

        if packet_received:
            rssi = self.get_rssi()
            data_length = self.spi_read(Register.FIFO)
            data = self.spi_burst_read(Register.FIFO, data_length)

            self.log.info("Received message: %s, RSSI: %s", data, rssi)
            return (bytearray(data), rssi)
        else:
            return None

    def send_packet(self, data, preamble=None):
        data = bytearray(data)

        if self.config.packet_config_1.variable_length:
            data = [len(data)] + list(data)

        self.log.debug("Initialising Tx...")
        start = time()
        self.set_mode(OpMode.TX)

        while not self.read_register(IRQFlags1).tx_ready:
            sleep(0.005)

        self.log.debug("In Tx mode (took %.3fs)", time() - start)

        if preamble:
            sleep(preamble)

        self.write_fifo(data)

        while not self.read_register(IRQFlags2).packet_sent:
            sleep(0.005)

        self.set_mode(OpMode.Standby)
        self.log.debug("Packet (%r) sent in %.3fs", data, time() - start)

    def set_mode(self, mode):
        start = time()
        self.config.opmode.mode = mode
        self.write_register(self.config.opmode)
        while True:
            irqflags = self.read_register(IRQFlags1)
            if irqflags.mode_ready:
                duration = time() - start
                self.log.debug("Mode changed to %s in %.3fs", mode, duration)
                return
            sleep(0.005)

    def get_rssi(self):
        return -(self.spi_read(Register.RSSIVALUE) / 2)

    def read_temperature(self):
        self.set_mode(OpMode.Standby)
        reg = Temperature1()
        reg.start = True
        self.write_register(reg)
        while self.read_register(Temperature1).running:
            sleep(0.005)

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
