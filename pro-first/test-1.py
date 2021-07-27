#!/usr/bin/python3
import os,sys

name = "whole global name";

class HalMisc2(object):
    def __init__(self):
        print("HalMisc2 -----__init__")
        # self.misc = HalMisc()

    def test_1(self):
        print("HalMisc2    test_1")
        # HalMisc().morton_test_2()
        # self.misc.morton_test_1()
    def test_2(self):
        print("HalMisc2    test_2")


class HalMisc(HalMisc2):
    name2 = "HalMisc1--name2"
    def __init__(self):
        self.name = "matao---HalMisc"
        name1 = "matao---HalMisc1"
        # print("HalMisc -----__init__")
        print(name1)
        self.enable_power_force_ctrl = "0x88"
        self.disable_power_force_ctrl = "0x99"

    def setUp(self):
        print("test -----1")
    

    def load_config(self, config_file=None):              #None可以允许不带参数
        print(config_file)
        if not config_file:
            print("not config_file")
        print("over")

    def morton_test_1(self):
        HalMisc2().test_2()
        print("morton_test_1")

    def morton_test_2(self):
        print("morton_test_2")
        var = self.disable_power_force_ctrl
        print("morton_test_2",var)

    def get_name(self):
        print(name)
        # print(name2)
        print(self.name)
        print(self.name2)










print("test 123")
HalMisc().morton_test_1()

# HalMisc().load_config("123")

# HalMisc().load_config()
# HalMisc().morton_test_2()

# print("test none")
# HalMisc2().test_1()

# HalMisc().get_name()

# print("test========format===============")
# test_0 = "morton0"
# test_1 = "morton1"
# test_2 = "morton2"
# test_3 = "morton3"
# test = "morton::{0}{2}{1}{3}".format(test_0, test_1, test_2, test_3)

# print(test)