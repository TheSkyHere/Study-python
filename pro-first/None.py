#!/usr/bin/python3
import os,sys

def load_config(config_file=None):              #None可以允许不带参数

    print(config_file)
    if not config_file:
        print("not config_file")

    print("over")



print("test 123")
load_config("123")
print("test none")
load_config()