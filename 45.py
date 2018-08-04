# -*- coding:utf-8 -*-
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
         
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length_pHead1 = self.getLinklistLength(pHead1)
        length_pHead2 = self.getLinklistLength(pHead2)
        diff = 0
        p_start = None
        p_wait = None
         
        if length_pHead1 >= length_pHead2: # 注意这里别忘了"="
            diff = length_pHead1 - length_pHead2
            p_start = pHead1
            p_wait = pHead2
        elif length_pHead1 < length_pHead2:
            diff = length_pHead2 - length_pHead1
            p_start = pHead2
            p_wait = pHead1
            
        while diff > 0:
            p_start = p_start.next
            diff -= 1
            
        while p_start != None and p_wait != None and p_start != p_wait:
            p_start = p_start.next
            p_wait = p_wait.next
            
        return p_start
    
    def getLinklistLength(self, pHead):
        link_list_length = 0
        pNode = pHead
        while pNode != None:
            link_list_length += 1
            pNode = pNode.next
        return link_list_length