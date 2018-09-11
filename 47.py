# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 非递归写法
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        last = None
        while pHead:
            tmp = pHead
            pHead = pHead.next
            tmp.next = last
            last = tmp
        return last
    

class Solution2(object):
    # 递归写法
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        
        new_head = self.ReverseList(pHead.next)
        pHead.next.next = head
        pHead.next = None
        return new_head
