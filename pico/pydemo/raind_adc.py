# 雨滴探测传感器

from machine import Pin, ADC
from time import sleep

pin_do = Pin(15, Pin.IN)
pin_ao = ADC(0) # ADC0/GP26

state = 1
while True:
    va = pin_ao.read_u16()
    print(f'read {va}')
    
    vd = pin_do.value()
    if vd != state:
        if vd == 1:
            print('not raining')
        if vd == 0:
            print('raining')
        state = vd
    sleep(1)
    