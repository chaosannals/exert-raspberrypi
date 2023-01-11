# Nrf24l01 从机
# 找到角落的 GND ，引脚如下
# GND | VCC3.3
# ————|
# CE    CSN
# SCK   MOSI
# MISO  IRQ

import usys
import ustruct as struct
import utime
from machine import Pin, SPI
from nrf24l01 import NRF24L01
from micropython import const

# Slave pause between receiving data and checking for further packets.
_RX_POLL_DELAY = const(15)
# Slave pauses an additional _SLAVE_SEND_DELAY ms after receiving data and before
# transmitting to allow the (remote) master time to get into receive mode. The
# master may be a slow device. Value tested with Pyboard, ESP32 and ESP8266.
_SLAVE_SEND_DELAY = const(10)

if usys.platform == "pyboard":
    cfg = {"spi": 2, "miso": "Y7", "mosi": "Y8", "sck": "Y6", "csn": "Y5", "ce": "Y4"}
elif usys.platform == "esp8266":  # Hardware SPI
    cfg = {"spi": 1, "miso": 12, "mosi": 13, "sck": 14, "csn": 4, "ce": 5}
elif usys.platform == "esp32":  # Software SPI
    cfg = {"spi": -1, "miso": 32, "mosi": 33, "sck": 25, "csn": 26, "ce": 27}
elif usys.platform == "rp2":  # PI PICO
    cfg = {"spi": 0, "miso": 4, "mosi": 7, "sck": 6, "csn": 14, "ce": 17}
else:
    raise ValueError("Unsupported platform {}".format(usys.platform))

# 地址是小头格式. 转化成大头。
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")

def slave():
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
    if cfg["spi"] == -1:
        spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
        nrf = NRF24L01(spi, csn, ce, payload_size=8)
    else:
        nrf = NRF24L01(SPI(cfg["spi"]), csn, ce, payload_size=8)

    nrf.open_tx_pipe(pipes[1])
    nrf.open_rx_pipe(1, pipes[0])
    nrf.start_listening()

    print("NRF24L01 slave mode, waiting for packets... (ctrl-C to stop)")

    while True:
        if nrf.any():
            while nrf.any():
                buf = nrf.recv()
                millis, led_state = struct.unpack("ii", buf)
                print("received:", millis, led_state)
                #for led in leds:
                #    if led_state & 1:
                #        led.on()
                #    else:
                #        led.off()
                #    led_state >>= 1
                #utime.sleep_ms(_RX_POLL_DELAY)

            # Give master time to get into receive mode.
            #utime.sleep_ms(_SLAVE_SEND_DELAY)
            nrf.stop_listening()
            try:
                nrf.send(struct.pack("ii", millis, led_state))
            except OSError:
                pass
            print("sent response", millis)
            nrf.start_listening()

slave()
