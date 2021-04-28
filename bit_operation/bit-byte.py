#!/usr/bin/python3
import sys,os



# 则&， |表示位运算， and，or则依据是否非0来决定输出，
num = 3&1
print("3&1=",num)
num = 3&2
print("3&2=",num)
num = 3&3
print("3&3=",num)

num = 2|1
print("2|1=",num)
num = 3|0
print("3|0=",num)
num = 4|3
print("4|3=",num)


# 判断变量是否为0， 是0则为False，非0判断为True，
# and中含0，返回0； 均为非0时，返回后一个值， 
# 2 and 0   # 返回0
# 2 and 1   # 返回1
# 1 and 2   # 返回2
num = 2 and 1
print("2 and 1=",num)
num = 3 and 0
print("3 and 0=",num)
num = 4 and 3
print("4 and 3=",num)


# # or中， 至少有一个非0时，返回第一个非0,
# 2 or 0   # 返回2
# 2 or 1   # 返回2
# 0 or 1   # 返回1 
num = 2 or 1
print("2 or 1=",num)
num = 3 or 0
print("3 or 0=",num)
num = 4 or 3
print("4 or 3=",num)



