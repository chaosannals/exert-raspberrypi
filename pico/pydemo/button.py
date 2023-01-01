from machine import Pin
from time import sleep

class Button:
    def __init__(self, gpio_number):
        self.pin = Pin(gpio_number, Pin.IN, Pin.PULL_UP)
        self.is_press = False
        self.is_loose = False
        self.is_toggle = False
        self.is_down = False
        self.value = 1
        
    def update(self):
        v = self.pin.value()
        self.is_down = v == 0
        self.is_toggle = v != self.value
        self.is_press = self.is_toggle and v == 0
        self.is_loose = self.is_toggle and v == 1
        self.value = v
        
button_up = Button(10)
button_left = Button(11)
button_down = Button(12)
button_right = Button(13)

print('start')
while True:
    button_up.update()
    button_left.update()
    button_down.update()
    button_right.update()
    
    if button_up.is_press:
        print('press up')
    if button_up.is_loose:
        print('loose up')
        
    if button_left.is_press:
        print('press left')
    if button_left.is_loose:
        print('loose left')
        
    if button_down.is_press:
        print('press down')
    if button_down.is_loose:
        print('loose down')
        
    if button_right.is_press:
        print('press right')
    if button_right.is_loose:
        print('loose right')
    sleep(0.02)

