from machine import Pin
from time import sleep

relay = Pin(15, Pin.OUT)
relay.value(0)

while True:
    relay.value(1)
    sleep(0.5)
    relay.value(0)
    sleep(0.5)
    