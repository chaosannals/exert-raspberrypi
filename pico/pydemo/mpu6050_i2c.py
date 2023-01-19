# 陀螺仪

from machine import I2C, Pin
from mpu6050 import MPU6050
from time import sleep, ticks_us, ticks_diff
from math import sqrt, asin

imu = MPU6050(I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))
imu.sample_rate = 39 # g: 8000Hz / (1 + 39) = 200Hz  a: 1000Hz / (1 + 39) = 25Hz
imu.accel_range = 0 # ±2g 16bit 
imu.gyro_range = 0 # 250°/s 16bit

gx = 0
gy = 0
gz = 0
while True:
    # TODO 计算位移和转向
    ax = imu.accel.x / 0x4FFF # 0xFFFF / 4g
    ay = imu.accel.y / 0x4FFF
    az = imu.accel.z / 0x4FFF
    
    vx = ax * 0.
    
    gx += imu.gyro.x
    gy += imu.gyro.y
    gz += imu.gyro.z
    tem = round(imu.temperature, 2)
    
    gdim = sqrt(gx*gx + gy*gy + gz*gz)
    gax = asin(gx / gdim)
    gay = asin(gy / gdim)
    gaz = asin(gz / gdim)
    
    
    print(f'v:({vx},{vy},{vz}) g({gax},{gay},{gaz}) t: {tem}')
    sleep(0.2)
    