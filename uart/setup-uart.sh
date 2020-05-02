#/bin/bash

echo BB-UART1 > /sys/devices/platform/bone_capemgr/slots
echo BB-UART2 > /sys/devices/platform/bone_capemgr/slots
echo BB-UART3 > /sys/devices/platform/bone_capemgr/slots
echo BB-UART4 > /sys/devices/platform/bone_capemgr/slots

# config-pin P9.21 uart # UART2_TXD
# config-pin P9.22 uart # UART2_RXD Grove connector

sleep 5
cat /sys/devices/platform/bone_capemgr/slots

python3.7 src/sensor.py
