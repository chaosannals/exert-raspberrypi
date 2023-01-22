# 舵机
# VCC V5

from machine import Pin, PWM
from time import sleep
from math import floor

HZ = 50 # 20ms 一周期
MIN = floor(0xFFFF / 20 * 0.5) # 0.5 ms 的占空比 -90°
MIDDLE = floor(0xFFFF / 20 * 1.5) # 1.5 ms 占空比 0°
MAX = floor(0xFFFF / 20 * 2.5) # 2.5 ms 的占空比  90°


pwm = PWM(Pin(0))
pwm.freq(HZ)


pwm.duty_u16(MIN)
sleep(4)
pwm.duty_u16(MIDDLE)
sleep(4)
pwm.duty_u16(MAX)
