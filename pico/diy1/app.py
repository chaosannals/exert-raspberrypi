from machine import Pin, SPI
from time import sleep
from drive.st7735s import TFT


def tft_init(spi=SPI(0, sck=Pin(2), mosi=Pin(3)), cs=5, dc=6, reset=7):
    t = TFT(spi, dc, reset, cs)
    print("TFT Initializing")
    t.initg()
    t.fill(0)
    return t

def tft_do(t: TFT):
    t.fill(t.RED)
    sleep(1)
    t.fill(t.BLUE)
    sleep(1)
    t.fill(t.GREEN)

tft = tft_init()
tft_do(tft)