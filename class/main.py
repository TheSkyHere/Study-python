#!/usr/bin/env python3

import unittest,os

from mode_class1 import (
    class1,
)
# from mode_A import mode_A_class

main_class_val = "main_class_val"
key = "7777"
value = "12312312"
class main_class(class1):
    # main_class_val = "main_class_val_self"
    # def __init__(self):
    #     print("this is main_class init")
    def main(self):
        print("main",main_class_val)
        # print("main---self",self.main_class_val)

    def main1(self):
        self.fun_class1()

    def main2(self):
        self.fun_class2()

    def main3(self):
        self.fun_class3()

    def main4(self):
        print("Morton=====test Sensor={}, reported value={}".format(key, value))

    def main4(self):
        self.fun2_class1()
        mode_A_class().fun_mode_A_class()
        print("test=======over======")
    



# main_class().main()
# main_class().main1()
# main_class().main2()
# main_class().main3()
# mode_A_class().fun_mode_A_class()

# main_class().main4()
main_class().main4()