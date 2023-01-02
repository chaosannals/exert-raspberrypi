# 震颤开关

from machine import Pin
from time import sleep

pin_vibrate = Pin(13, Pin.IN, Pin.PULL_UP)
pin_red = Pin(15, Pin.OUT)
pin_green = Pin(14, Pin.OUT)
pin_red.value(1)
pin_green.value(0)

def led_toggle():
    pin_red.toggle()
    pin_green.toggle()
    
# 通过循环没有用到中断，其实用中断更好吧。
state = 0
while True:
    if pin_vibrate.value() == 1:
        state = state + 1
        if state > 1:
            state = 0
            
        led_toggle()
        print(f'vibrate {state}')