# 霍尔传感器
# 与干簧管区别是可以感应磁场南北。

from machine import Pin, ADC
from time import sleep

adc_hall = ADC(0) # GP26/ADC0
pin_hall = Pin(27, Pin.IN, Pin.PULL_UP)# GP27

while True:
    ao = adc_hall.read_u16()
    do = pin_hall.value()
    print(f'ao: {ao} do: {do}')
    sleep(1)