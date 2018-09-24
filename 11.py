# -*- coding: utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        
        ugly_number_count = 1
        ugly_number_list = [1]
        ugly2index = 0
        ugly3index = 0
        ugly5index = 0
        
        while ugly_number_count < index:
            ugly_number_list.append(min(ugly_number_list[ugly2index] * 2,
                                        ugly_number_list[ugly3index] * 3,
                                        ugly_number_list[ugly5index] * 5))
            
            last_number = ugly_number_list[len(ugly_number_list)-1]
            while ugly_number_list[ugly2index] * 2 <= last_number:
                ugly2index += 1
            while ugly_number_list[ugly3index] * 3 <= last_number:
                ugly3index += 1
            while ugly_number_list[ugly5index] * 5 <= last_number:
                ugly5index += 1
                
            ugly_number_count += 1
        
        return ugly_number_list[len(ugly_number_list)-1]


# 1. 欧几里得算法：gcd(a,b) = gcd(b,a mod b) (不妨设a>b 且r=a mod b ,r不为0)。
# def func(a, b):
#     if a < b:
#         a = a ^ b
#         b = a ^ b
#         a = a ^ b
#
#    while a % b != 0:
#        tmp = a % b
#        a = b
#        b = tmp
#
#    return b
