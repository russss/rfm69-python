# rfm69-python

A library to control HopeRF RFM69-series radio modules through SPI and
GPIO. This is designed for use on a Raspberry Pi but might also work on
similar hardware (such as Beaglebone Black) with appropriate tweaks.

Written for use with the [ukhas.net](http://ukhas.net) project.

## Requirements
* Only currently tested on python 2.7, may also work on 3.4+

## Datasheets
* [RFM69W](http://www.hoperf.com/upload/rf/RFM69W-V1.3.pdf)
* [Semtech SX1231](https://www.semtech.com/images/datasheet/sx1231.pdf)
    (the underlying RF chip, which much of the RFM69 datasheet is lifted
    from)

## Prior Art
* [UKHASNetPiGateway](https://github.com/dbrooke/UKHASNetPiGateway) (in
  C/Wiring)
* [ukhasnet LPC810 node](https://github.com/jamescoxon/LPC810)
* [Python code for the beaglebone black](https://github.com/wcalvert/rfm69-python)
