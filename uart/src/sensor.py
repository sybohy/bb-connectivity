#!/usr/bin/env python3.7

# import Adafruit_BBIO.UART as UART
import os
import time

# UART.setup("UART2")

while(True):
    time.sleep(15)

    print("\n")

    # # ADC121C021 address, 0x50(80)
    # # Read data back from 0x00(00), 2 bytes
    # # raw_adc MSB, raw_adc LSB
    # data = bus.read_i2c_block_data(0x50, 0x00, 2)
    #
    # # Convert the data to 12-bits
    # raw_adc = (data[0] & 0x0F) * 256 + data[1]
    #
    # # Output data to screen
    # print("Digital Value of Analog Input : ",  raw_adc)
