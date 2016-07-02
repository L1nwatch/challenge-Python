#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

import math

__author__ = '__L1n__w@tch'


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return x * y / gcd(x, y)


def get_the_two_num(number_gcd, number_lcm):
    a_list = []
    tmp = number_lcm / number_gcd
    for a in range(int(math.sqrt(tmp)), 0, -1):
        if tmp % a == 0:
            b = tmp / a
            if gcd(a, b) == 1:
                a_list.append(a * number_gcd)
                a_list.append(b * number_gcd)
                break

    return a_list


if __name__ == '__main__':
    num_gcd = 4
    num_lcm = 16
    List = get_the_two_num(num_gcd, num_lcm)
    List.sort()
    print("%d %d" % (List[0], List[1]))
