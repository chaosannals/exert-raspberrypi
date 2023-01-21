# RFID
# MFRC522 读

from mfrc522_spi import MFRC522

mfrc = MFRC522(0, sck=2, mosi=3, miso=4, cs=5, rst=6)

try:
    while True:
        (stat, tag_type) = mfrc.request(mfrc.REQIDL)
        if stat == mfrc.OK:
            print('reqidl success')
            (stat, raw_uid) = mfrc.anticoll()

            if stat == mfrc.OK:
                print(f'tag type: {tag_type} raw uid: {raw_uid}')

                if mfrc.select_tag(raw_uid) == mfrc.OK:
                    key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,] # 默认密码
                    if mfrc.auth(mfrc.AUTHENT1A, 8, key, raw_uid) == mfrc.OK:
                        print(f"address 8 data: {mfrc.read(8)}")
                        mfrc.stop_crypto1()
                    else:
                        print('auth failed')
                else:
                    print('select tag failed')
except Exception as e:
    print(e)