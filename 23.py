# -*- coding:utf-8 -*-
class Solution:
    # 和我的思路想符的写法，时间复杂度为O(mn)，如果使用Python语言编写不能通过。
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        flags = [None] * n
        count = n
        step = 0
        i = -1

        while count > 0:
            i += 1
            if i >= n: i = 0
            if flags[i] == 1: continue
            step += 1
            if step == m:
                step = 0
                count -= 1
                flags[i] = 1

        return i

    def LastRemaining_Solution2(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


# 本题实际上就是约瑟夫环问题,记住公式:
#                  0         , n = 1
# f(n, m)= [f(n-1, m)+m] % n , n > 1
#
# 参考: http://zhedahht.blog.163.com/blog/static/2541117420072250322938/