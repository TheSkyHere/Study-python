#!/usr/bin/python3
import os,sys

name = "whole global name";

class HalMisc2(object):
    def test_1(self):
        self.set_psu_cmd()
        print(self.psu_cmd)
        # HalMisc().morton_test_2()
        # self.misc.morton_test_1()
    def test_2(self):
        print("HalMisc2    test_2")


class HalMisc(HalMisc2):
    def set_psu_cmd(self):
        self.psu_cmd = "/usr/bin/psu-util"
        self.psu_id = 2










print("test 123")
HalMisc().test_1()

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