# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        flag = [False] * len(matrix)
        for i in xrange(rows):
            for j in xrange(cols):
                if self.helper(matrix, rows, cols, path, i, j, 0, flag):
                    return True
        return False

    def helper(self, matrix, rows, cols, path, x, y, k, flag):
        index = x * cols + y
        if x < 0 or x >= rows or \
            y < 0 or y >= cols or \
            matrix[index] != path[k] or \
            flag[index]:
            return False

        if k == len(path) - 1:
            return True

        flag[index] = True

        if self.helper(matrix, rows, cols, path, x - 1, y, k + 1, flag) or \
            self.helper(matrix, rows, cols, path, x + 1, y, k + 1, flag) or \
            self.helper(matrix, rows, cols, path, x, y - 1, k + 1, flag) or \
            self.helper(matrix, rows, cols, path, x, y + 1, k + 1, flag):
            return True

        flag[index] = False
        return False


# 注意matrix是一个一维数组