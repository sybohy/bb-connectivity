#!/usr/bin/env python3.7

import adafruit_mlx90640
import board
import busio
import math
import os
import json
import logging
from logging.handlers import RotatingFileHandler
import time

PIXEL_WIDTH = int(os.environ.get("PIXEL_WIDTH"))
PIXEL_HEIGHT = int(os.environ.get("PIXEL_HEIGHT"))
file = os.environ.get("SENSOR_LOG_FILE")

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768
while True:
  try:
    mlx.getFrame(frame)
  except ValueError:
    # these happen, no biggie - retry
    continue
  print(frame)
  data = [{
    'x': i % (PIXEL_WIDTH-1),
    'y': math.floor(i/PIXEL_HEIGHT),
    'value': value
  } for i,value in enumerate(frame)]
  with open(file, 'w') as filetowrite:
    filetowrite.write(json.dumps(data))
