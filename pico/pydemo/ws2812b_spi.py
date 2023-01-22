# RGB 灯
# WS2812b

import gc
from machine import SPI, Pin
from time import sleep

class WS2812:
    """
    Driver for WS2812 RGB LEDs. May be used for controlling single LED or chain
    of LEDs.

    Example of use:

        chain = WS2812(spi_bus=1, led_count=4)
        data = [
            (255, 0, 0),    # red
            (0, 255, 0),    # green
            (0, 0, 255),    # blue
            (85, 85, 85),   # white
        ]
        chain.show(data)

    Version: 1.0
    """
    buf_bytes = (0x88, 0x8e, 0xe8, 0xee)
    # WS2812 没有时钟线，所以都是靠时长
    # 0 码： 高电平220ns-420ns 低电平 750ns~1600ns
    # 1 码： 高电平750ns~1600ns 低电平 220ns~420ns
    # 利用 SPI 该频率下传输数据时电平高低
    # 3200000Hz 大概 312.5ns 正好在 220ns~420ns 之间；312.5ns * 3 也在 750ns~1600ns 之间
    # 所以 0 码可以用 0x8 表示  1 码用 0xe 表示。
    # 正好可以1字节数据传输 2 个码
    # 0x88 = 0b10001000 就是 00
    # 0x8e = 0b10001110 就是 01
    # 0xe8 = 0b11101000 就是 10
    # 0xee = 0b11101110 就是 11

    def __init__(self, spi_bus=1, led_count=1, intensity=1):
        """
        Params:
        * spi_bus = SPI bus ID (1 or 2)
        * led_count = count of LEDs
        * intensity = light intensity (float up to 1)
        """
        self.led_count = led_count
        self.intensity = intensity

        # prepare SPI data buffer (4 bytes for each color)
        self.buf_length = self.led_count * 3 * 4
        self.buf = bytearray(self.buf_length)

        # SPI init
        self.spi = SPI(spi_bus, mosi=Pin(3))
        self.spi.init(baudrate=3200000, polarity=0, phase=1)

        # turn LEDs off
        self.show([])

    def show(self, data):
        """
        Show RGB data on LEDs. Expected data = [(R, G, B), ...] where R, G and B
        are intensities of colors in range from 0 to 255. One RGB tuple for each
        LED. Count of tuples may be less than count of connected LEDs.
        """
        self.fill_buf(data)
        self.send_buf()

    def send_buf(self):
        """
        Send buffer over SPI.
        """
        self.spi.write(self.buf)
        gc.collect()

    def update_buf(self, data, start=0):
        """
        Fill a part of the buffer with RGB data.

        Order of colors in buffer is changed from RGB to GRB because WS2812 LED
        has GRB order of colors. Each color is represented by 4 bytes in buffer
        (1 byte for each 2 bits).

        Returns the index of the first unfilled LED

        Note: If you find this function ugly, it's because speed optimisations
        beated purity of code.
        """

        buf = self.buf
        buf_bytes = self.buf_bytes
        intensity = self.intensity

        mask = 0x03 # 0b11 就是只有 0-3 确保不超过 buf_bytes 的长度
        index = start * 12 # 1byte 传 2bit 所以 8bit 需要 4byte，RGB 3色 合计 12byte
        for red, green, blue in data:
            red = int(red * intensity)
            green = int(green * intensity)
            blue = int(blue * intensity)

            buf[index] = buf_bytes[green >> 6 & mask]
            buf[index+1] = buf_bytes[green >> 4 & mask]
            buf[index+2] = buf_bytes[green >> 2 & mask]
            buf[index+3] = buf_bytes[green & mask]

            buf[index+4] = buf_bytes[red >> 6 & mask]
            buf[index+5] = buf_bytes[red >> 4 & mask]
            buf[index+6] = buf_bytes[red >> 2 & mask]
            buf[index+7] = buf_bytes[red & mask]

            buf[index+8] = buf_bytes[blue >> 6 & mask]
            buf[index+9] = buf_bytes[blue >> 4 & mask]
            buf[index+10] = buf_bytes[blue >> 2 & mask]
            buf[index+11] = buf_bytes[blue & mask]

            index += 12

        return index // 12

    def fill_buf(self, data):
        """
        Fill buffer with RGB data.

        All LEDs after the data are turned off.
        """
        end = self.update_buf(data)

        # 如果 data 没有设置所有的灯的颜色，补0
        # turn off the rest of the LEDs
        buf = self.buf
        off = self.buf_bytes[0]
        for index in range(end * 12, self.buf_length):
            buf[index] = off
            index += 1
            
            
chain = WS2812(spi_bus=0, led_count=4)
data = [
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (85, 85, 85),   # white
]
chain.show(data)
sleep(4)
data.reverse()
chain.show(data)
sleep(4)
chain.show([])
