# -*- coding: utf-8 -*-


class Solution(object):
    def func(self, s):
        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 26:
                return 2
            return 1

        return self.func(s[1:]) + (self.func(s[0:2])-1) * self.func(s[2:])


print Solution().func('12258')

# self.func(s[0:2])-1    这里为什么要减一呢？
#
# 因为减治法分为前后两部分，self.func(s[1:])这里已经包括前面是1个数的部分，所以要减一。
#
# if int(s) <= 26: return 2    这里为什么要返回2呢，不返回1呢？
#
# 因为要右边为两个字符的时候