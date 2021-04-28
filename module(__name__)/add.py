#!/usr/bin/python3
import os,sys

def add(a,b):
    return a+b
def fun_add_4_7():
    print("fun_add_4_7 run ")
    num = add(4,7)
    print("num=",num)

if __name__ == "__main__":   #if not add this code than __name__.py call add() will run fun_add_4_7()
    fun_add_4_7()
    