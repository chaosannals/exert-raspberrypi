# Nrf24l01 主机
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


def master():
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
    if cfg["spi"] == -1:
        spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
        nrf = NRF24L01(spi, csn, ce, payload_size=8)
    else:
        nrf = NRF24L01(SPI(cfg["spi"]), csn, ce, payload_size=8)

    nrf.open_tx_pipe(pipes[0])
    nrf.open_rx_pipe(1, pipes[1])
    nrf.start_listening()

    num_needed = 16
    num_successes = 0
    num_failures = 0
    led_state = 0

    print("NRF24L01 master mode, sending %d packets..." % num_needed)

    while num_successes < num_needed and num_failures < num_needed:
        # stop listening and send packet
        nrf.stop_listening()
        millis = utime.ticks_ms()
        led_state = max(1, (led_state << 1) & 0x0F)
        print("sending:", millis, led_state)
        try:
            nrf.send(struct.pack("ii", millis, led_state))
        except OSError:
            pass

        # start listening again
        nrf.start_listening()

        # wait for response, with 250ms timeout
        start_time = utime.ticks_ms()
        timeout = False
        while not nrf.any() and not timeout:
            if utime.ticks_diff(utime.ticks_ms(), start_time) > 250:
                timeout = True

        if timeout:
            print("failed, response timed out")
            num_failures += 1

        else:
            # recv packet
            (got_millis,got_state) = struct.unpack("ii", nrf.recv())

            # print response and round-trip delay
            print(
                "got response:",
                got_millis,
                got_state,
                "(delay",
                utime.ticks_diff(utime.ticks_ms(), got_millis),
                "ms)",
            )
            num_successes += 1

        # delay then loop
        utime.sleep_ms(250)

    print("master finished sending; successes=%d, failures=%d" % (num_successes, num_failures))
    
master()