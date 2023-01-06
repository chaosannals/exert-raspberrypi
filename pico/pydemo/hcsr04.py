# 声波距离探测器 HCSR04

from machine import Pin
from time import sleep, sleep_us, ticks_us

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)

while True:
    trigger.value(0)
    sleep_us(2)
    trigger.value(1)
    sleep_us(5)
    trigger.value(0)
    while echo.value() == 0:
        start_at = ticks_us()
    while echo.value() == 1:
        end_at = ticks_us()
    duration = end_at - start_at
    distance = (duration * 0.0343) / 2 # 音速乘以时间 / 2
    print(f'distance: {distance}cm')
    sleep(1)
