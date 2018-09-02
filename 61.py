# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        
        pPre = None
        self.helper(pRootOfTree, [pPre])
        
        res = pRootOfTree
        while res.left:
            res = res.left
        return res
        
    def helper(self, pCurr, pPre):
        if pCurr == None:
            return None
        
        self.helper(pCurr.left, pPre)
        pCurr.left = pPre[0]
        if pPre[0] != None:
            pPre[0].right = pCurr
        pPre[0] = pCurr
        self.helper(pCurr.right, pPre)