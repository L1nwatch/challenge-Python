#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 题目描述
输出100以内的所有素数，素数之间以一个空格区分
"""
import gmpy2

__author__ = '__L1n__w@tch'


def solve1():
    """
    如果允许用 gmpy2 库就好说了
    :return:
    """
    for i in range(100):
        if gmpy2.is_prime(i):
            if i != 2:
                print(end=" ")
            print(i, end="")


def solve2():
    def _is_sushu(num):
        for i in range(num):
            if i == 0 or i == 1:
                continue
            if num % i == 0:
                return False
        return True

    for i in range(101):
        if i == 0 or i == 1:
            continue
        if _is_sushu(i):
            print(i, end=" ")


if __name__ == "__main__":
    # solve1()
    # solve2()
    pass
