# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead==None or pHead.next==None or pHead.next.next==None:
            return None
        low=pHead.next
        fast=pHead.next.next
        while low!=fast: # 这里是关键，判断链表中是否有环
            if fast.next==None or fast.next.next==None:
                return None
            low=low.next
            fast=fast.next.next
        fast=pHead
        while low!=fast:
            low=low.next
            fast=fast.next
        return fast


# 思路见牛客答案。