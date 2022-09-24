"""
Created on Thur Aug 25 11:41 2022

@author: zhang
"""

# PyMath计算器3.4.1
# 使用须知：
# 1.本产品由Zhang Wenzhou于2022年8月研发
# 2.开放源代码 https://github.com/ZhangWzhou/ZhangWenzhou/blob/main/PyMath%E8%AE%A1%E7%AE%97%E5%99%A83.4.py
# 3.免费

print("欢迎使用PyMath计算器 3.4.1!")
print("本计算器提供算术运算：加法（+）、减法（-）、乘法（*）、除法（/）、取余除（%）、取整除（//）、乘方（**）、开方（sqrt()）八种运算；逻辑运算："
      "and，or，not三种运算；比较运算：>=，==，<=,>，<五种运算；转换类型：int()整数类型、float()浮点类型、str()字符串类型。")
print("可以调用NumPy（模块名np）、Pandas（模块名pd）、random（模块名rd）函数。")
print("提供科学绘图(matplotlib)，使用时模块名使用plt。注意：一个提示符后只能写一行代码！不可对变量进行赋值！")
print("可以调用π(pi)。")
print("如果看到>>>提示符即可输入运算表达式，按回车运算。")
print("如需终止运算请输入exit()。")
print("---------------------------------------------------------------------------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import sqrt, pi
import random as rd

while True:
    a = input(">>>")
    if a == "exit()":
        break
    if a == "":
        print(" ")
        pass
    else:
        print(eval(a))
    pass
pass
