# 无源蜂鸣器

from machine import Pin, PWM
from time import sleep

CL = [0, 131, 147, 165, 175, 196, 211, 248] # 低C调
CM = [0, 262, 294, 330, 350, 393, 441, 495] # 中C调
CH = [0, 525, 589, 661, 770, 786, 882, 990] # 高C调

TONE_1 = [
    CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],
    CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
    CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
    CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5],
]

# 1 代表 1/8 拍
BEAT_1 = [
    1, 1, 3, 1, 1, 3, 1, 1,
    1, 1, 1, 1, 1, 1, 3, 1,
    1, 3, 1, 1, 1, 1, 1, 1,
    1, 2, 1, 1, 1, 1, 1, 
]

SONG_2 = [
    (CM[1],1), (CM[1],1), (CM[1],2), (CL[5],2),
    (CM[3],1), (CM[3],1), (CM[3],2), (CM[1],2),
    
    (CM[1],1), (CM[3],1), (CM[5],2), (CM[5],2),
    (CM[4],1), (CM[2],1), (CM[2],3), (CM[2],1),
    
    (CM[3],1), (CM[4],2), (CM[4],2), (CM[3],1),
    (CM[2],1), (CM[3],2), (CM[1],2), (CM[1],1),
    
    (CM[3],1), (CM[2],2), (CL[5],2), (CL[7],1),
    (CM[2],1), (CM[1],1),
]

pwm_buzzer = PWM(Pin(12))

def sing(tone, beat):
    for i in range(1, len(tone)):
        # 音符
        pwm_buzzer.duty_u16(1000)
        pwm_buzzer.freq(tone[i])
        sleep(beat[i] * 0.5)
    pwm_buzzer.duty_u16(0)

def sing_song(song):
    for s in song:
        pwm_buzzer.duty_u16(1000)
        pwm_buzzer.freq(s[0])
        sleep(s[1] * 0.5)
    pwm_buzzer.duty_u16(0)


print('start 1')
sing(TONE_1, BEAT_1)
print('stop 1')
sleep(2)
print('start 2')
sing_song(SONG_2)
print('stop 2')
