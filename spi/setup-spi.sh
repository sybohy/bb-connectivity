#/bin/bash

modprobe i2c-dev
export I2C_BUS=1

python3.7 src/sensor.py
