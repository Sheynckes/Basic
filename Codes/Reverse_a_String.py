# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 17:08
# @Author  : SHeynckes
# @Email   : shenghai@ymail.com
# @File    : Reverse_a_String.py
# @Software: PyCharm

# 把一个字符串按单词翻转（需保留所用空格）——面试常见
# 先把字符串中的每个单词翻转，然后再把整个字符串翻转。
# 注：如果使用split()方法，则无法处理对空格的要求。

setence = '  Hello, how are you?    Fine.    '


# 定一个辅助函数
def reverse(str_list, start, end):
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1


str_list = list(setence)
i = 0

while i < len(str_list):
    if str_list[i] != ' ':
        start = i
        end = start + 1
        while (end < len(str_list)) and str_list[end] != ' ':
            end += 1
        reverse(str_list, start, end - 1)
        i = end
    else:
        i += 1

str_list.reverse()
print(''.join(str_list))
