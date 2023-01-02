#有源蜂鸣器

from machine import Pin
from time import sleep

pin_buzzer = Pin(12, Pin.OUT)
pin_buzzer.value(1)

print('start')
for _ in range(10):
    print('beep')
    pin_buzzer.value(0) # ON
    sleep(2)
    pin_buzzer.value(1) # OFF
    sleep(1)
    
pin_buzzer.value(1)
print('stop')