# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k == 0:
            return None

        res = []
        self.helper(pRoot, res)
        
        if k > len(res):
            return None
        return res[k-1]
        
    def helper(self, pRoot, res):
        if pRoot != None:
            self.helper(pRoot.left, res)
            res.append(pRoot)
            self.helper(pRoot.right, res)