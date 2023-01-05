# 声音传感器

from machine import Pin, ADC
from time import sleep

adc_sound = ADC(0) # GP26/ADC0
pin_sound = Pin(27, Pin.IN, Pin.PULL_UP)# GP27

while True:
    ao = adc_sound.read_u16()
    do = pin_sound.value()
    print(f'ao: {ao} do: {do}')
    sleep(1)