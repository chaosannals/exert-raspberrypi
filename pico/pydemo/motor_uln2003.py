# 马达  电机
# ULN2003 电流MAX 500mA 电压MAX 50V


from machine import Pin
from time import sleep

pin = Pin(0, Pin.OUT)

print('start')
pin.value(1)
sleep(10)
pin.value(0)
print('stop')
