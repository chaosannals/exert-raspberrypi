# TM1637 显示
from machine import Pin
from time import sleep_us, sleep

# MSB B7...B0 （注：无关位为 0） 
# 控制字节最高 2 位 B7 B6 是 控制指令类型
CMD_DATA   =0b01000000 # 数据指令 B1 为 1 读键盘（显示无关） B2 为 1 固定地址模式 0 为自动增地址模式 B3 0 普通模式 1 测试模式
CMD_DISPLAY=0b10000000 # 显示指令 显示指令最低3位 B2 B1 B0 代表 亮度值只支持 8 个级别 0 - 7
CMD_ADDRESS=0b11000000 # 地址指令 低3位 B2 B1 B0 指定地址，6个地址 0 - 5

# 显示指令 B3（第4位） 是否显示 1 显示 0 不显示
CMD_DISPLAY_OPEN = 0b1000

TM1637_DELAY=10

# 数据被写入地址后会显示出来 0 - 3 地址
# 地址的数据 前7位 分别 B0 - B6 位 对应 7 个灯位
#     B0
#  B5     B1
#     B6
#  B4     B2
#     B3

class TM1637:
    def __init__(self, gp_clk=1, gp_dio=0, brightness=7):
        self.clock_pin = Pin(gp_clk)
        self.data_pin = Pin(gp_dio)
        self.brightness = brightness & 0b111 # 显示指令最低3位 B2 B1 B0 代表 亮度值只支持 8 个级别 0 - 7
        self.clock_pin.init(Pin.OUT, value=0)
        self.data_pin.init(Pin.OUT, value=0)
 
        sleep_us(TM1637_DELAY)

        self.write_data_cmd()
        self.open_display()
        
    def _start(self):
        self.data_pin.value(0)
        sleep_us(TM1637_DELAY)
        self.clock_pin.value(0)
        sleep_us(TM1637_DELAY)
        
    def _stop(self):
        self.data_pin.value(0)
        sleep_us(TM1637_DELAY)
        self.clock_pin.value(1)
        sleep_us(TM1637_DELAY)
        self.data_pin.value(1)
        
    def _write_byte_and_ack(self, v):
        for i in range(8):
            b = (v >> i) & 1
            self.data_pin.value(b)
            sleep_us(TM1637_DELAY)
            self.clock_pin.value(1)
            sleep_us(TM1637_DELAY)
            self.clock_pin.value(0)
            sleep_us(TM1637_DELAY)
        # ack
        self.clock_pin.value(0)
        sleep_us(TM1637_DELAY)
        self.clock_pin.value(1)
        sleep_us(TM1637_DELAY)
        self.clock_pin.value(0)
        sleep_us(TM1637_DELAY)
        
    def write_data_cmd(self):
        self._start()
        self._write_byte_and_ack(CMD_DATA)
        self._stop()
        
    def open_display(self):
        self._start()
        self._write_byte_and_ack(CMD_DISPLAY | CMD_DISPLAY_OPEN | self.brightness)
        self._stop()
        
    def write(self, v):
        self.write_data_cmd()
        
        self._start()
        self._write_byte_and_ack(CMD_ADDRESS)
        for i in range(4):
            self._write_byte_and_ack(v[i])
        self._stop()
        
        self.open_display()
        
tm = TM1637()

print('start')

b = 0
for i in range(7):
    b = b | (1 << i)
    tm.write([b for i in range(4)])
    sleep(1)

print('stop')

