# -*- coding: utf-8 -*-
class Solution(object):
    def movingCount(self, threshold, rows, cols):
        flag = map(lambda cols: [False for i in range(cols)], [cols] * rows) # 这里注意
        return self.helper(0, 0, threshold, rows, cols, flag)

    def helper(self, x, y, threshold, rows, cols, flag):
        if x < 0 or x >= rows or y < 0 or y >= cols or + \
            self.numSum(x) + self.numSum(y) > threshold or flag[x][y]:
            return 0

        flag[x][y] = True

        return self.helper(x, y + 1, threshold, rows, cols, flag) + \
            self.helper(x, y - 1, threshold, rows, cols, flag) + \
            self.helper(x - 1, y, threshold, rows, cols, flag) + \
            self.helper(x + 1, y, threshold, rows, cols, flag) + 1

    def numSum(self, num):
        sum = 0
        while num != 0:
            sum += num % 10
            num /= 10
        return sum


# *注意Python中如何创建二维数组*