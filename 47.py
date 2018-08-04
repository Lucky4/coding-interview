# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        p = pHead
        if p == None:
            return None
        
        q = pHead.next
        if q == None:
            return p
        
        r = q.next
        if r == None:
            q.next = p
            p.next = None
            return q
        
        q.next = p
        p.next = None
        p = q
        q = r
        r = r.next
        while r != None:
            q.next = p
            p = q
            q = r
            r = r.next
            
        q.next = p
        return q


# 我的解决思路最先处理了第一个节点，稍有些复杂。更高效的方式应该从None开始构造一个逆置的链表。
# class Solution:
#     def ReverseList(self, pHead):
#         if not pHead or not pHead.next:
#             return pHead

#         last = None
#         while pHead:
#             tmp = pHead.next
#             pHead.next = last
#             last = pHead
#             pHead = tmp
#         return last