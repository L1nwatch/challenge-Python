#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 杨辉三角
题目描述:
还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
..............
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如n=2,则输出：
1
1 1


# 记得自己在ACM写过，不过顿时想不起来了，
# 看了ACM之家的题解，发现全都是记录上一层然后求出这一层的，没有其他好方法，那么就这样吧
# 以下是看着ACM的C++杨辉三角写的http://www.acmerblog.com/hdu-2032-3119.html
"""

__author__ = '__L1n__w@tch'


def get_num(row, col, num):
    if col == 0 or col == row:
        num[row][col] = 1
    if num[row][col] == -1:
        num[row][col] = get_num(row - 1, col - 1, num) + \
                        get_num(row - 1, col, num)

    return num[row][col]


def solve(n, number_array):
    for i in range(n):
        for j in range(i):
            print(get_num(i, j, number_array), end=' ')  # 2.X版本:print(getNum(i, j, num_array)),
        print(get_num(i, i, number_array), end='\n')  # 2.X版本print(getNum(i, i, num_array))


def create_num_array(n):
    num = []
    for i in range(n):
        num.append([-1 for i in range(n)])

    return num


if __name__ == "__main__":
    for n in range(1, 20):
        num_array = create_num_array(n)
        solve(n, num_array)
