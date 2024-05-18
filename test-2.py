import datetime
import binascii
import subprocess


def int32_to_string(int32):
    str = ''
    for i in range(4):
        byte = (int32 >> (8 * (3 - i))) & 0xff
        str += chr(byte)
    str = binascii.hexlify(str.encode())
    str = ' '.join([f"0x{str[i:i+2].decode()}" for i in range(0, 8, 2)])
    return str


timestamp_ms = int(datetime.datetime.now().timestamp() * 1000 // 1)

# 将毫秒级时间戳转换为对应的天数和剩余的毫秒数
days, milliseconds = divmod(timestamp_ms, 86400000)
print("days:", days)
print("milliseconds:", milliseconds)

days_str = int32_to_string(days)
milliseconds_str = int32_to_string(milliseconds)

subprocess.run("i2cset -f -y 0 0x47 0xD7 0x08 {} {} i".format(milliseconds_str, days_str), shell=True)
