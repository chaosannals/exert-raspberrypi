from machine import Pin
from utime import sleep

leds = [Pin(i, Pin.OUT) for i in range(0,8)]

while True:
    for n in range(0,8):
        leds[n].value(1)
        sleep(0.05)
    for n in range(0,8):
        leds[n].value(0)
        sleep(0.05)