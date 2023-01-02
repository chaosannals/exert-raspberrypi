from machine import Pin, PWM
from time import sleep

# COLORS = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
COLORS = [0xFF00, 0x0440]

pwm_red = PWM(Pin(15))
pwm_green = PWM(Pin(14))

pwm_red.freq(1000)
pwm_green.freq(1000)

def scale_round(x, min_in, max_in, min_out, max_out):
    range_out = max_out - min_out
    range_in = max_in - min_in
    range_rate = range_out / range_in
    scale_x = (x - min_in) * range_rate
    return round(scale_x + min_out)

def set_color(color):
    red = scale_round(color >> 8, 0, 0xFF, 0, 0xFFFF)
    green = scale_round(color & 0xFF, 0, 0xFF, 0, 0xFFFF)
    pwm_red.duty_u16(red)
    pwm_green.duty_u16(green)
    

while True:
    for color in COLORS:
        set_color(color)
        sleep(0.5)