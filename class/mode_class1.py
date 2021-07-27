#!/usr/bin/env python3

import unittest,os
from mode_A import mode_A_class

from mode_class2 import (
    class2,
)


# Global variables
mode_class1 = "Global_mode_class1"

class class1(class2):
    # main_class_val = "main_class_val_selfclass1"
    # def __init__(self):
    #     print("this is class1 init")
    def fun_class1(self):
        print("this is class1",main_class_val)
    def fun2_class1(self):
        print("this is class1",mode_class1)
        mode_A_class().fun_mode_A_class()