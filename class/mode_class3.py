#!/usr/bin/env python3

import unittest,os
from mode_A import mode_A_class


# Global variables
mode_class3 = "Global_mode_class3"

class class3():
    mode_class3 = "mode_class3222222222"
    # def __init__(self):
    #     print("this is class3 init")
    def fun_class3(self):
        print("this is class3",mode_class3)
        mode_A_class().fun_mode_A_class()