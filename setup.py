from __future__ import division, absolute_import, print_function, unicode_literals
from setuptools import find_packages, setup

setup(name="rfm69",
      version="0.2",
      description="Library for accessing the HopeRF RFM69-series radio modules via GPIO/SPI.",
      author="Russ Garrett",
      author_email='russ@garrett.co.uk',
      platforms=["any"],
      license="MIT",
      url="http://github.com/russss/rfm69-python",
      packages=find_packages(),
      install_requires=[
          'enum >= 0.4.6',
          'RPi.GPIO >= 0.6.0',
          'spidev >= 3.0'
      ]
      )
