#!/usr/bin/python3
import os,sys
from aiohttp.web import Application


str1 = "<.PlainResource  /api/sys/vddcore"
str2 = "."
  

# print (str1.index(str2))#结果5
# print (str1.index(str2, 2))#结果5
# print (str1.index(str2, 3))#结果报错，没找到子字符串



print (str1.index(str2))
#结果5

print (str1[:str1.index(str2)])     
#获取 "."之前的字符(不包含点)  结果 Hello

print (str1[str1.index(" "):]) 
#获取 "."之前的字符(包含点) 结果.python


rest_route_path = str1[str1.index("  "):].split("/")
print (rest_route_path) 
#获取 "."之前的字符(包含点) 结果.python