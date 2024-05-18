#!/usr/bin/python3
import subprocess

# 执行show_version脚本并获取输出
output = subprocess.check_output("cat ./show_version", shell=True, universal_newlines=True)


# 创建一个空字典来存储版本信息
dict_bmc_info = {}

# 使用字符串处理操作将输出按行拆分并处理每一行
lines = output.strip().split("\n")
for line in lines:
    # 按照冒号(:)拆分每一行，获取键和值
    key, value = line.split(":")
    # 去除键和值的前后空格
    key = key.strip()
    value = value.strip()
    # 将键值对添加到字典中
    dict_bmc_info[key] = value

# 打印字典中的版本信息
for key, value in dict_bmc_info.items():
    print(key + ": " + value)