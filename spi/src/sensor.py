#!/usr/bin/env python3

import Adafruit_BBIO.SPI import SPI
import time

spi = SPI(0,0)

while(True):
    time.sleep(0.5)

    print("Digital Value of SPI sensor : ",  "abc")
