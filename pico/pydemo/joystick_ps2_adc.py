# PS2 操纵杆

from machine import Pin, ADC
from time import sleep

adc_x = ADC(0,) # ADC0/GP26
adc_y = ADC(1) # ADC1/GP27
pin_sw = Pin(28, Pin.IN, Pin.PULL_UP) # GP28

x = 0
y = 0
sw = 0

def adc_round(adc):
    # 值会飘，所以把精度调低，就不会飘得很厉害。
    return round(adc.read_u16() / 0xFFFF * 0xF)

while True:
    now_x = adc_round(adc_x)
    now_y = adc_round(adc_y)
    now_sw = pin_sw.value()
    
    if now_x != x or now_y != y:
        print(f'({x}, {y})')
        x = now_x
        y = now_y
        
    if now_sw != sw:
        if now_sw == 0:
            print(f'press {now_sw}')
        else:
            print(f'loose {now_sw}')
        sw = now_sw
    