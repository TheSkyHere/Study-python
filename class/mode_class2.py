#!/usr/bin/env python3

import unittest,os

from mode_class3 import (
    class3,
)

# Global variables
mode_class2 = "Global_mode_class2"


class class2(class3):
    # def __init__(self):
    #     print("this is class2 init")
    def fun_class2(self):
        print("this is class2",mode_class2)