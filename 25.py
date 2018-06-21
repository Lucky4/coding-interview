# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        tmp_stack = []
        for i in range(0, len(pushV)):
            tmp_stack.append(pushV[i])
            if tmp_stack[-1] == popV[0]:
                while len(tmp_stack) and tmp_stack[-1] == popV[0]:
                    tmp = tmp_stack.pop()
                    popV.remove(tmp)
        if len(tmp_stack) > 0:
            return False
        return True