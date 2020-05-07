#!/usr/bin/env python3

import Adafruit_BBIO.SPI as SPI
import time

spi_zero = SPI(1,0)
spi_one = SPI(1,1)

while(True):
    time.sleep(0.5)

    print("Digital Value of SPI sensor : ",  "abc")
