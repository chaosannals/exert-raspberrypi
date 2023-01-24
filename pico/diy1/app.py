from machine import Pin, SPI
from time import sleep
from struct import unpack, pack
from drive.st7735s import TFT
from drive.nrf24l01 import NRF24L01


def tft_init(spi=SPI(0, sck=Pin(2), mosi=Pin(3)), cs=5, dc=6, reset=7):
    t = TFT(spi, dc, reset, cs)
    print("TFT Initializing")
    t.initg()
    t.fill()
    return t

def tft_do(t: TFT):
    sleep(1)
    t.fill(t.RED)
    sleep(1)
    t.fill(t.BLUE)
    sleep(1)
    t.fill(t.GREEN)

tft = tft_init()
tft_do(tft)

# 地址，小头格式
PIPES = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")

def nrf_listen(spi=SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12)), cs=13, ce=14):
    nrf = NRF24L01(
        spi,
        cs=Pin(cs),
        ce=Pin(ce),
        payload_size=8
    )
    nrf.open_tx_pipe(PIPES[1])
    nrf.open_rx_pipe(1, PIPES[0])
    nrf.start_listening()
    print('start listen')
    while True:
        if nrf.any():
            while nrf.any():
                buf = nrf.recv()
                millis, led_state = unpack('ii', buf)
                print(f'received: {millis} {led_state}')
            nrf.stop_listening()
            try:
                nrf.send(pack('ii', millis, led_state))
            except OSError:
                pass
            print(f'send response: {millis}')
            nrf.start_listening()
            
nrf_listen()