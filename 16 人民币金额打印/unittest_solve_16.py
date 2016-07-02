#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 测试自己的答案是否正确
"""
import unittest
from solve_16 import solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def test(self):
        self.failUnless(solve(55555) == "伍万伍仟伍佰伍拾伍圆")
        self.failUnless(solve(0) == "零圆")
        self.failUnless(solve(99999999) == "玖仟玖佰玖拾玖万玖仟玖佰玖拾玖圆")
        self.failUnless(solve(12) == "壹拾贰圆")
        self.failUnless(solve(234) == "贰佰叁拾肆圆")
        self.failUnless(solve(3456) == "叁仟肆佰伍拾陆圆")
        self.failUnless(solve(45678) == "肆万伍仟陆佰柒拾捌圆")
        self.failUnless(solve(567890) == "伍拾陆万柒仟捌佰玖拾圆")
        self.failUnless(solve(6789012) == "陆佰柒拾捌万玖仟零壹拾贰圆")
        self.failUnless(solve(78901234) == "柒仟捌佰玖拾万壹仟贰佰叁拾肆圆")
        self.failUnless(solve(10000) == "壹万圆")
        self.failUnless(solve(100000) == "壹拾万圆")
        self.failUnless(solve(1000000) == "壹佰万圆")





if __name__ == "__main__":
    pass
