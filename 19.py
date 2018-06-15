# -*- coding:utf-8 -*-
class Solution:
    # 动态规划，自底向上
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2

        first = 1
        second = 2
        third = 0

        for i in range(3, number+1):
            third = first + second
            first = second
            second = third

        return third

#我的笨方法
# def jumpFloor(self, number):
#     if number == 1:
#         return 1
#     elif number == 2:
#         return 2
#     return self.jumpFloor(number-1) + self.jumpFloor(number-2)
#
# 动态规划可以看看https://zhuanlan.zhihu.com/p/31628866



