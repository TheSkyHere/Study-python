#!/usr/bin/python3
import os,sys

print("test========format===============")
test_0 = "morton0 "
test_1 = "morton1 "
test_2 = "morton2 "
test_3 = "morton3 "
test = "morton: {0}{2}{1}{3}".format(test_0, test_1, test_2, test_3)

print(test)