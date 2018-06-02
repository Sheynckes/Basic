# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 17:02
# @Author  : SHeynckes
# @Email   : shenghai@ymail.com
# @File    : Computational Efficiency.py
# @Software: PyCharm

# 以求和计算为例，比较Python中不同方法（求和算法和数据类型）的计算效率。
# 可以看出，利用numpy库中的sum()函数对numpy库中的array数据类型进行求和，计算效率会得到大幅度提高。

import timeit

# 利用for循环求和
sum_by_for = """
for d in data:
    s += d
"""

# 利用Python自带的sum()函数求和
sum_by_sum = """
sum(data)
"""

# 利用numpy库中的sum()函数求和
sum_by_numpy_sum = """
import numpy
numpy.sum(data)
"""


# 对list数据类型求和
def timeit_using_list(n, loops):
    # n为从1加到几
    # loops为循环次数
    list_setup = """
data = [1] * {}
s = 0
""".format(n)
    print('list result:')
    print(timeit.timeit(sum_by_for, list_setup, number=loops))
    print(timeit.timeit(sum_by_sum, list_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum, list_setup, number=loops))


# 对array数据类型求和
def timeit_using_array(n, loops):
    # n为从1加到几
    # loops为循环次数
    array_setup = """
import array
data = array.array('L', [1] * {})
s = 0
""".format(n)
    print('array result:')
    print(timeit.timeit(sum_by_for, array_setup, number=loops))
    print(timeit.timeit(sum_by_sum, array_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum, array_setup, number=loops))


# 对numpy数据类型求和
def timeit_using_numpy(n, loops):
    # n为从1加到几
    # loops为循环次数
    numpy_setup = """
import numpy
data = numpy.array([1] * {})
s = 0
""".format(n)
    print('numpy result:')
    print(timeit.timeit(sum_by_for, numpy_setup, number=loops))
    print(timeit.timeit(sum_by_sum, numpy_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum, numpy_setup, number=loops))


if __name__ == '__main__':
    timeit_using_list(30000, 500)
    timeit_using_array(30000, 500)
    timeit_using_numpy(30000, 500)