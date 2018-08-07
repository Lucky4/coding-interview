# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        
        if pHead and not pHead.next:
            return pHead
        
        p_distinct_head = p_distinct_curr = ListNode(-1)
        p_curr = pHead
        pre_val = None
        
        while p_curr.next:
            if p_curr.val == p_curr.next.val:
                pre_val = p_curr.val
                p_curr = p_curr.next.next
                if not p_curr:
                    break
            else:
                tmp = p_curr.next
                p_curr.next = None
                p_distinct_curr.next = p_curr
                p_distinct_curr = p_distinct_curr.next
                p_curr = tmp
                
        if p_curr and not p_curr.val == pre_val:
            p_distinct_curr.next = p_curr
            
        return p_distinct_head.next