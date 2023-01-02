from machine import Pin
from time import sleep

pin_button = Pin(13, Pin.IN, Pin.PULL_UP)
pin_red = Pin(15, Pin.OUT)
pin_green = Pin(14, Pin.OUT)

def led_toggle():
    pin_red.toggle()
    pin_green.toggle()
    
def on_button_down(chn):
    led_toggle()
    if pin_button.value() == 0:
        print('press')
        
pin_button.irq(trigger=Pin.IRQ_FALLING, handler=on_button_down)

while True:
    sleep(1)
        

