# 红外探头

from machine import Pin
from time import sleep

pin = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    v = pin.value()
    print(v) # 0 是有反射信息了。
    sleep(0.2)