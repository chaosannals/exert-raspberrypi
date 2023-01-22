# 人体热释电感
# VCC 5V

from machine import Pin
from time import sleep

pin = Pin(0, Pin.IN, Pin.PULL_UP)
pin.value(1)

old_v = 1
while True:
    v = pin.value()
    if v != old_v:
        print(f'v: {v}')
        old_v = v
    sleep(0.1)