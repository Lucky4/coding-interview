# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print1(self, pRoot):
        res = []
        if pRoot == None:
            return res
        
        q = deque()
        q.append(pRoot)
        while len(q) > 0:
            tmp_rec = []
            q_size = len(q)
            while q_size > 0:
                tmp = q.popleft()
                tmp_rec.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                q_size -= 1
            res.append(tmp_rec)
            
        return res

    def Print2(self, pRoot):
        res = []
        if pRoot == None:
            return res
        
        tmp_res = []
        q = deque()
        q.append(pRoot)
        start = 0
        end = 1
        while len(q) > 0:
            tmp = q.popleft()
            tmp_res.append(tmp.val)
            start += 1
            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)
            if start == end:
                res.append(tmp_res)
                tmp_res = []
                start = 0
                end = len(q)
                
        return res


# 第一种方法比较好理解复杂度为O（N2），第二种复杂度为O（N）。