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
            res_list.append(res)

        for j in range(i, len(ss_list)):
            self.swap(ss_list, i, j)
            self.Helper(ss_list, i + 1, res_list)
            self.swap(ss_list, i, j)
            
    def swap(self, res_list, i, j):
        tmp = res_list[i]
        res_list[i] = res_list[j]
        res_list[j] = tmp


# 疑问：swap(self, res_list, i, j)函数如果写成swap(self, i, j)这种形式，为什么没有起到交换作用？
#   答：swap(self, i, j)函数被调用后，实参通过赋值传递给形参，传递的是对象（引用类型），
#       我们的i，j是局部变量，指向不可变类型，对i，j赋值对实参没有影响；对i，j操作时对可变参数会产生影响
# 
#
# 解法2：使用Python内置的itertools.permutations排列方法，要记住itertools中常用的方法。
# import itertools
# class Solution:
#     def Permutation(self, ss):
#         if not ss:
#             return []
#         return sorted(list(set(map(''.join, itertools.permutations(ss)))))
#
#
# 解法3：该问题还可使用减治的思想。后续有时间补充。（ps：估计是不会补充了。。）
