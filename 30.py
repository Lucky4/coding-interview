# -*- coding: utf-8 -*-
class Solution(object):
    def Palindromic(selfs, s):
        s = list(s)

        if len(s) == 0:
            return 0

        pre_list = []
        pre_list.append(1)
        count = 1

        for i in range(1, len(s)):
            curr_list = []
            curr_list.append(1)

            if s[i] == s[i - 1]:
                curr_list.append(2)

            for j in pre_list:
                if i - j - 1 >= 0 and s[j] == s[i - j - 1]:
                    curr_list.append(j + 2)

            count += len(curr_list)
            pre_list = curr_list

        return count