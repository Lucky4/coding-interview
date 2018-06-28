# -*- coding:utf-8 -*-
class Solution:
    # 基于回溯的思想
    def Permutation(self, ss):
        if len(ss) == 0:
            return []

        ss_list = list(ss)
        res_list = []
        self.Helper(ss_list, 0, res_list)
        res_list.sort()
        
        return res_list
        
    def Helper(self, ss_list, i, res_list):
        if i == len(ss_list) - 1:
            res = ''.join(ss_list)
            if res not in res_list:
                res_list.append(res)

        for j in range(i, len(ss_list)):
            self.swap(ss_list, i, j)
            self.Helper(ss_list, i + 1, res_list)
            self.swap(ss_list, i, j)
            
    def swap(self, res_list, i, j):
        tmp = res_list[i]
        res_list[i] = res_list[j]
        res_list[j] = tmp


# 疑问1：swap(self, res_list, i, j)函数如果写成swap(self, i, j)这种形式，为什么没有起到交换作用？
# 答：因为swap()函数中i，j都是形参，函数内为参数赋予新值不会改变外部任何变量，其中的运行机制相当于，swap()函数获得主函数实参的拷贝。
# 
# 解法2：使用Python内置的itertools.Permutations排列方法，要记住itertools中常用的方法。
# import itertools
# class Solution:
#     def Permutation(self, ss):
#         if not ss:
#             return []
#         return sorted(list(set(map(''.join, itertools.permutations(ss)))))
#
# 解法3：该问题还可使用减治的思想。后续有时间补充。（ps：估计是不会补充了。。）
