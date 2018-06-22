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

    # 冒泡思想,写在这里主要是熟悉下冒泡操作.
    # def reOrderArray(self, array):
    #     for i in range(0, len(array) - 1):
    #         for j in range(0, len(array) - i - 1):
    #             if array[j] & 1 == 0 and array[j + 1] & 1 == 1:
    #                 array[j] = array[j] ^ array[j + 1]
    #                 array[j + 1] = array[j] ^ array[j + 1]
    #                 array[j] = array[j] ^ array[j + 1]
    #     return array



# 1. 学习判断偶数的高效写法.
# 2. 注意循环中变量索引是否超出范围.