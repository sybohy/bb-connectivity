#/bin/bash

config-pin P9.21 uart # UART2_TXD
config-pin P9.22 uart # UART2_RXD Grove connector

python3.7 src/sensor.py
