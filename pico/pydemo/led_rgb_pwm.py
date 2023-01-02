from machine import Pin, PWM
from time import sleep

COLORS = [
    0xff0000,
    0x00ff00,
    0x0000ff,
    0xffff00,
    0xff00ff,
    0x00ffff,
]

pwm_red = PWM(Pin(11))
pwm_green = PWM(Pin(12))
pwm_blue = PWM(Pin(13))

# 需要的电流不同所以频率不同
pwm_red.freq(2000)
pwm_green.freq(1999)
pwm_blue.freq(5000)

def scale_round(x, min_in, max_in, min_out, max_out):
    range_out = max_out - min_out
    range_in = max_in - min_in
    range_rate = range_out / range_in
    scale_x = (x - min_in) * range_rate
    return round(scale_x + min_out)

def led_off():
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)
    
def set_color(color):
    red = scale_round((color & 0xff0000) >> 16, 0, 0xff, 0, 0xffff)
    green = scale_round((color & 0x00ff00) >> 8, 0, 0xff, 0, 0xffff)
    blue = scale_round((color & 0x0000ff) >> 0, 0, 0xff, 0, 0xffff)
    
    pwm_red.duty_u16(red)
    pwm_green.duty_u16(green)
    pwm_blue.duty_u16(blue)
    
print('start')
for color in COLORS:
    set_color(color)
    sleep(1)
led_off()
print('stop')