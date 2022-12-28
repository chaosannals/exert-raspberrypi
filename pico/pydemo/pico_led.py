from machine import Pin, Timer, lightsleep

led = Pin(25, Pin.OUT) # pico 唯一的 LED 灯
timer = Timer() # 计时器

def blink(timer):
    '''
    回调
    '''
    print('blick')
    led.toggle()

# 初始化计时器，程序会每秒0.5次的频率触发。
timer.init(freq=0.5, mode=Timer.PERIODIC, callback=blink)

# 这里主程序等待
lightsleep(10000)

# 回收计时器
timer.deinit()

# 灯灭
led.value(0)
print('deinit')