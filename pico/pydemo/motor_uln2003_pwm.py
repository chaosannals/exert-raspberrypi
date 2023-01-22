# 马达  电机
# ULN2003 电流MAX 500mA 电压MAX 50V


from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(0))
pwm.freq(40)


print('start')

print('lv: 1')
pwm.duty_u16(0x4FFF)
sleep(4)
print('lv: 2')
pwm.duty_u16(0x8FFF)
sleep(4)
print('lv: 3')
pwm.duty_u16(0xBFFF)
sleep(4)
print('lv: 4')
pwm.duty_u16(0xFFFF)
sleep(4)
pwm.duty_u16(0x000F)
sleep(4)
print('stop')
