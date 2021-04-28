#!/usr/bin/python3
import os,sys


# read() 用法：
# 从文件当前位置起读取size个字节，若无参数size，则表示读取至文件结束为止，它范围为字符串对象。

# readline()用法：
# 该方法每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。

# readlines()用法：
# 读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。

#strip()用于去除字符串首尾的字符，默认是空格、\n、\t

#Python引入了with语句来自动帮我们调用close()方法：

print("test ===readline()===")
with open("./test.log",'r') as f:        
    status = f.readline().strip()
    print("1--readline().strip()=",status)
    status = f.readline().strip()       #讲读取第二行
    print("2--readline().strip()=",status)
print("\n")

print("test ===strip()===")
with open("./test.log",'r') as f:        #其中6为这一行的前6个字符（注意strip()）
    status = f.readline().strip()       
    print("1--readline().strip()=",status)
with open("./test.log",'r') as f:        
    status = f.readline()
    print("1--readline()XXXXXX()=",status)
print("\n")

print("test ===readlines()===")
with open("./test.log",'r') as f:   
    status = f.readlines()            
    print("--------readlines()=",status)
with open("./test.log",'r') as f:   
    status = f.readlines(2)            
    print("--------readlines(2)=",status)
with open("./test.log",'r') as f:   
    status = f.readlines(4)            
    print("--------readlines(4)=",status)
print("\n")

print("test ===read()===")
with open("./test.log",'r') as f:   
    status = f.read(6)            #其中6为这一行的前6个字符（注意strip()）
    print("--------read(6)=",status)

with open("./test.log",'r') as f:   
    status = f.read(30)            #其中6为这一行的前6个字符（注意strip()）
    print("--------read(30)=",status)
print("\n")