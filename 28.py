# -*- coding:utf-8 -*-
class Solution:
    # 前面是偶数,后面是奇数,奇数与偶数交换,中间可能有多个偶数,顺序将其右移.
    def reOrderArray(self, array):
        for i in range(0, len(array) - 2):
            if not self.isEven(array[i]):
                continue

            j = i + 1
            while j !=len(array) and self.isEven(array[j]):
                j += 1

            if j < len(array):
                tmp = array[j]
                while j != i:
                    array[j] = array[j - 1]
                    j -= 1
                array[j] = tmp
            else:
                break

        return array

    def isEven(self, number):
        return not number & 1

#这个题要重做


# 1. 学习判断偶数的高效写法.
# 2. 注意循环中变量索引是否超出范围.
