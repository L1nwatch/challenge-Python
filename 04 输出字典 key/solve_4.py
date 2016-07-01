#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 题目描述:
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。
"""

__author__ = '__L1n__w@tch'


def solve1(a):
    """
    这种方法打出来老是有空格
    """
    i = 0
    length = len(a)
    for each in a:
        i += 1
        print(each, end='')
        if i < length:
            print(end=',')


def solve2(a):
    """
    :return:
    """
    b = [str(i) for i in a]
    print(','.join(b))


def solve3(a):
    """
    一句话, 可读性差了些
    :param a:
    :return:
    """
    print(",".join([str(i) for i in a]))


if __name__ == "__main__":
    a = {1: 1, 2: 2, 3: 3}
    solve3(a)
