# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return None
        
        k_node = last_node = head
        while k > 0:
            if not last_node:
                return None
            last_node = last_node.next
            k -= 1
                
        while last_node:
            last_node = last_node.next
            k_node = k_node.next
        
        return k_node