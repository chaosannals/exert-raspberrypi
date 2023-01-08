# 红外激光头
from machine import Pin
from time import sleep

laser = Pin(15, Pin.OUT)
laser.value(0)

for _ in range(10):
    laser.value(1)
    sleep(1)
    laser.value(0)
    sleep(1)
    
laser.value(0)