# 旋转编码器
# 旋钮是一格一格的，每次跳格，CLK 和 DT 2个触点先后接通产生信号
# 通过判断触电的信号变动判断转动格数和方向。
# 卡中间了 会导致 2个触点都是 1。

from machine import Pin
from time import sleep

pin_clk = Pin(0, Pin.IN) # 触电0，用作时钟信号
pin_dt = Pin(1, Pin.IN) # 触电1，用作数据信号
pin_sw = Pin(2, Pin.IN, Pin.PULL_UP) # 轴中按钮

counter = 0

def on_sw_irq(chn):
    counter = 0
    print(f'sw: {counter}')

pin_sw.irq(trigger=Pin.IRQ_FALLING, handler=on_sw_irq)

counter_temp = 0
state_old = 0
state_now = 0
while True:
    state_old = pin_dt.value()
    flag = 0
    
    # 固定获取 CLK 的信号 1 （导通）时 DT 的前后信号值
    # 如果 0 1 认为是正转  1  0  反转（方向自己定）
    while not pin_clk.value():
        state_now = pin_dt.value()
        flag = 1
    if flag == 1:
        if state_old == 0 and state_now == 1:
            counter += 1
        elif state_old == 1 and state_now == 0:
            counter -= 1
        else:
            # 此时 CLK 触点导通，倒是 DT 没过去，导致前后值一样。
            pass
            #print('卡中间了。')
        
    
    if counter_temp != counter:
        print(f'counter: {counter}')
        counter_temp = counter