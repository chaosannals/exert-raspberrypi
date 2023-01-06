# 触碰开关 TTP223B

from machine import Pin
from time import sleep

pin = Pin(0, Pin.IN)
count = 0

while count < 10:
    if pin.value() == 1:
        count += 1
        print(f'touch {count}')
    sleep(0.4)
    