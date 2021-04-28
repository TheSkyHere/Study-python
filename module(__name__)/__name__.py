#!/usr/bin/python3
import os,sys
# 所以，if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。

from add import *

def fun_test1():
    print("fun_test1 run")
    num = add(4,9)
    print("num = ",num)
fun_test1()