# 电位器

from machine import ADC
from time import sleep

adc = ADC(0)

while True:
    v = adc.read_u16()
    print(f'v {v}')
    sleep(1)