# -*- coding:utf-8 -*-
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)


# 这个题，对于我来说就是巩固正则表达式，学会使用正则表达式来解决问题。
# 有几个注意的地方：
# 1. 什么是科学计数法？
# 2. 为什么正则表达式中有[0-9]*，因为测试用例中有如：-.E10的测试用例。