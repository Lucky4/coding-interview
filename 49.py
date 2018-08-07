# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        
        curr = pHead
        while curr:
            node = RandomListNode(curr.label)
            node.next = curr.next
            curr.next = node
            curr = node.next
            
        curr = pHead
        while curr:
            node = curr.next
            if curr.random:
                node.random = curr.random.next
            curr = node.next
            
        clone_head = pHead.next
        curr = pHead
        tmp = None
        while curr.next: # 这里为什么去判断curr.next而不是去判断curr呢，因为下面会使用到tmp.next，最后curr指向了最后元素，tmp指向了None。
            tmp = curr.next
            curr.next = tmp.next
            curr = tmp
            
        return clone_head