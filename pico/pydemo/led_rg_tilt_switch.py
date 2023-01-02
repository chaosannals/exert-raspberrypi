# 倾斜开关

from machine import Pin
from time import sleep

pin_tilt = Pin(13, Pin.IN, Pin.PULL_UP)
pin_red = Pin(15, Pin.OUT)
pin_green = Pin(14, Pin.OUT)
pin_red.value(1)
pin_green.value(0)

def led_toggle():
    pin_red.toggle()
    pin_green.toggle()
    
def on_tilt_detect(chn):
    led_toggle()
    if pin_button.value() == 0:
        print('tilt')
        
pin_tilt.irq(trigger=Pin.IRQ_FALLING, handler=on_tilt_detect)

