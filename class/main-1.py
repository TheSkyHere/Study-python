#!/usr/bin/env python3

import unittest,os

from mode_class1 import (
    class1,
)
from mode_A import mode_A_class


class main_class():
    main_class_val = "main_class_val_self"

    def main(self):
        print("main",self.main_class_val)
        mode_A_class().fun_mode_A_class()
    



main_class().main()
