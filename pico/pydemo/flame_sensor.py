# 火焰探测器
# 原理：700nm - 1000nm 的红外线感应。

from machine import Pin, ADC
from time import sleep

pin_adc = ADC(0) # GP26/ADC0
pin_gp = Pin(27, Pin.IN, Pin.PULL_UP)# GP27

while True:
    ao = pin_adc.read_u16()
    do = pin_gp.value()
    print(f'ao: {ao} do: {do}')
    sleep(1)