# Raspberry Pi Pico

## [MicroPython](https://micropython.org/)

找到[下载](https://micropython.org/download/rp2-pico/) uf2 文件，路径变了的话自己搜下 Raspberry 应该可以找到。

1. 在没有插入 USB 到 PC 的时候按住 BOOTSEL 键不松，直到 USB 插入 PC 时松开 BOOTSEL 建。

2. 把下载的 uf2 文件复制到这个盘，开发板就会检测到并烧录进去。

3. 此时 设备管理器 可以看到 pico 的串口。

## [Thonny](https://thonny.org/)

工具 - 选项 - 解释器 - 配置成 Raspberry Pi Pico 的，然后选中串口。

现在脚本在 PC 直接点运行就可以（上载运行流程一步到位），低版本需要上载到版上运行（实在很麻烦，有时候上载还会失败但是没有提示，运行的时候感觉程序没变）。

## SDK

[pico-sdk](https://github.com/raspberrypi/pico-sdk)

## [awesome micropython](https://awesome-micropython.com/)


## 启动

micropython 默认执行根目录下 main.py 文件。
