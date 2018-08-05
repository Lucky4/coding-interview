# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
            
        p = pHead1
        q = pHead2
        r_start = r = None # 注意这里，r和r_start没有分配内存空间，执向的None，下面要做判断处理
        while p != None and q != None:
            if p.val <= q.val:
                tmp = p
                p = p.next
                tmp.next = None
                if r == None:   # 注意这里
                    r_start = r = tmp
                else:
                    r.next = tmp
                    r = r.next
            else:
                tmp = q
                q = q.next
                tmp.next = None
                if r == None:   # 注意这里
                    r_start = r = tmp
                else:
                    r.next = tmp
                    r = r.next
                
        if p != None:
            r.next = p
        elif q != None:
            r.next = q
        
        return r_start