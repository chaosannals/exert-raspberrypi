#28：步进电机的有效最大外径是28毫米
#B：表示是步进电机
#Y：表示是永磁式
#J：表示是减速型（减速比1:64）
#48：表示四相八拍

from machine import Pin
from time import sleep

HALF_STEP = [
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,1],
]
FULL_STEP = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
]

class Stepper:
    def __init__(self, a=0, b=1, c=2, d=3):
        self.half_index = 0
        self.full_index = 0
        self.pin = [
            Pin(a, Pin.OUT),
            Pin(b, Pin.OUT),
            Pin(c, Pin.OUT),
            Pin(d, Pin.OUT),
        ]
        for p in self.pin:
            p.value(0)
        
    def step_half(self):
        '''
        半拍，8 * 8 转子转一圈
        因为齿轮，转轴转一圈是 8 * 8 * 64 = 4096
        '''
        steps = HALF_STEP[self.half_index]
        self.half_index = (self.half_index + 1) % len(HALF_STEP)
        for i, p in enumerate(self.pin):
            v = steps[i]
            p.value(v)
    
    def step_full(self):
        '''
        全拍，8 * 4 转子转一圈
        因为齿轮，转轴转一圈是 8 * 4 * 64 = 2048
        '''
        steps = FULL_STEP[self.full_index]
        self.full_index = (self.full_index + 1) % len(FULL_STEP)
        for i, p in enumerate(self.pin):
            v = steps[i]
            p.value(v)
        
stepper = Stepper()

print('half')
for i in range(8*8*64):
    stepper.step_half()
    sleep(0.001) # 因为分 8 步转格子所以需要电流少些，间隔可以短。
    
print('full')
for i in range(8*4*64):
    stepper.step_full()
    sleep(0.004) # 间隔不能太小，不然电流不够，转不动。。

