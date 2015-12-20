from __future__ import division, absolute_import, print_function, unicode_literals
from setuptools import find_packages, setup

setup(name="rfm69",
            version="0.1",
            description="Library for accessing the HopeRF RFM69-series radio modules via GPIO/SPI.",
            author="Russ Garrett",
            author_email='russ@garrett.co.uk',
            platforms=["any"],
            license="BSD",
            url="http://github.com/russss/rfm69-python",
            packages=find_packages(),
            )
