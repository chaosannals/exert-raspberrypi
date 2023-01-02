from machine import Pin
from time import sleep

## 时间好像不准（没办法到 0.x us 级别），无法模拟周期

RED = (255, 0, 0)
ORANGE = (255,165, 0)
YELLOW = (255,150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0 ,130)
VIOLET = (138, 43, 226)

BLACK = (0,0,0)

COLORS = [
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    INDIGO,
    VIOLET,
]

class Ws2812b:
    def __init__(self, gpio_number=0, count=4):
        self.gpio_number= gpio_number
        self.count = count
        
    def __enter__(self):
        self.pin = Pin(self.gpio_number, Pin.OUT)
        return self
        
    def __exit__(self, ext_type, ext_value, traceback):
        self.put_color(BLACK)
    
    def put_color(self, color):
        gbr = [color[i] for i in range(2, -1, -1)]
        for c in gbr: # G B R
            for i in range(7, -1, -1): # 高位先发
                v = (c << i) & 1
                if v == 0:
                    self.pin.value(1)
                    sleep(0.0000004)
                    self.pin.value(0)
                    sleep(0.00000085)
                else:
                    self.pin.value(1)
                    sleep(0.0000008)
                    self.pin.value(0)
                    sleep(0.00000045)
                
    def put_reset(self):
        self.pin.value(0)
        sleep(0.00005)
        
    def show(self, color):
        self.put_reset()
        for i in range(self.count):
            self.put_color(color)
        self.put_reset()

print('start')
with Ws2812b() as ws2812b:
    for color in COLORS:
        ws2812b.show(color)
        sleep(1)
        print(f'show {color}')


