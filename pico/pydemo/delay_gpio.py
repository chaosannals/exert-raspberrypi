# 延迟

from time import ticks_us

def delay(n):
    for _ in range(n):
        pass
    
# start 到 end 啥也没有都要 9us
# 没办法更小的延时，micropython 解释器太慢了。
start = ticks_us()
# delay(1)
end = ticks_us()
print(f'{end-start}')
