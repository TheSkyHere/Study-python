#!/usr/bin/python3
import time
def sleeptime(hour,min,second):
        return hour * 3600 + min * 60 + second
a =1
sec=sleeptime(0, 0, 5)
while a == 1:
    time.sleep(sec)
    print('kaishizhixing')