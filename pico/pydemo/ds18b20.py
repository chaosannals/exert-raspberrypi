# 温度传感器 DS18B20
# TODO read ds18x20 source

from machine import Pin
from ds18x20 import DS18X20
from onewire import OneWire
from time import sleep_ms

ds = DS18X20(OneWire(Pin(0)))
roms = ds.scan()
print('found devices:', roms)

for i in range(10):
    ds.convert_temp()
    sleep_ms(750)
    for rom in roms:
        t = ds.read_temp(rom)
        print(f't: {t}')