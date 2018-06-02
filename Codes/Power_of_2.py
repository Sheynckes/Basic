# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 17:06
# @Author  : SHeynckes
# @Email   : shenghai@ymail.com
# @File    : Power_of_2.py
# @Software: PyCharm

# 判断任意一个数是否是2的n次方


def is_pow2(n):
    return (n & (n - 1)) == 0


print(is_pow2(16))
print(is_pow2(32))
print(is_pow2(33))
