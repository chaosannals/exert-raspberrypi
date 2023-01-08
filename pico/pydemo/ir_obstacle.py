# 红外避障探头
# 因为光速太快，所以只能检查是否有障碍物，距离不好测。

from machine import Pin
from time import sleep

pin = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    if 0 == pin.value():
        print('has obstacle')
    else:
        print('no obstacle')
    sleep(0.2)