# 干簧管 或 U 型光电传感器

from machine import Pin
from time import sleep

pin_reed = Pin(13, Pin.IN, Pin.PULL_UP)
pin_red = Pin(15, Pin.OUT)
pin_green =Pin(14, Pin.OUT)
pin_red.value(0)
pin_green.value(1)

def on_detect(chn):
    pin_red.toggle()
    pin_green.toggle()
    if pin_reed.value() == 0:
        print('reed detect')

pin_reed.irq(trigger=Pin.IRQ_FALLING, handler=on_detect)
