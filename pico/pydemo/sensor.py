from machine import Pin
from time import sleep

class Sensor:
    def __init__(self, gpio_number):
        self.pin = Pin(gpio_number, Pin.IN)
        self.is_toggle = False
        self.value = 1
        
    def update(self):
        v = self.pin.value()
        self.is_toggle = v != self.value
        self.value = v

sensor = Sensor(15)
print('start')
while True:
    sensor.update()
    
    if sensor.is_toggle:
        print(f'toggle {sensor.value}')
        
    sleep(0.02)
        