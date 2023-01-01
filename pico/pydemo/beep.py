from machine import Pin
from time import sleep

class Beeper:
    def __init__(self, gpio_number):
        self.gpio_number = gpio_number
        
    def __enter__(self):
        self.pin = Pin(self.gpio_number, Pin.OUT)
        self.pin.value(1)
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.pin = Pin(self.gpio_number, Pin.IN)
        
    def on(self):
        self.pin.value(0)
        
    def off(self):
        self.pin.value(1)
        
    def beep(self, duration=0.04):
        self.pin.value(0)
        sleep(duration)
        self.pin.value(1)

with Beeper(15) as beeper:
    for i in range(10):
        beeper.beep()
    
    beeper.on()
    sleep(1)
    beeper.off()
