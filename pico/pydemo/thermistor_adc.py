# 温度传感器
# 温度越高 AO 值越小， DO 在低于 临界温度 时变成 1

from machine import Pin, ADC
from time import sleep

adc_thermistor = ADC(0) # GP26/ADC0
pin_thermistor = Pin(27, Pin.IN, Pin.PULL_UP)# GP27

while True:
    ao = adc_thermistor.read_u16()
    do = pin_thermistor.value()
    print(f'ao: {ao} do: {do}')
    sleep(1)