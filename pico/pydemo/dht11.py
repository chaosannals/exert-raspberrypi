# 温湿探测器 DHT11
# TODO read dht source

from machine import Pin
from time import sleep
from dht import DHT11

sensor = DHT11(Pin(0))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f'temp: {temp}°C hum: {hum}%')
    sleep(2)
    