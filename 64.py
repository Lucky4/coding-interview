# # -*- coding:utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        res = []
        if pRoot == None:
            return res
        
        q = deque()
        q.append(pRoot)
        sub = []
        stack = []
        level = 1
        start = 0
        end = 1
        while len(q) > 0:
            if level % 2 != 0:
                tmp = q.popleft()
                start += 1
                sub.append(tmp)
                
                if tmp.left != None:
                    q.appendleft(tmp.left)
                if tmp.right != None:
                    q.appendleft(tmp.right)
            else:
                tmp = q.popleft()
                start += 1
                sub.append(tmp)

                if tmp.right != None:
                    stack.append(tmp.right)
                if tmp.left != None:
                    stack.append(tmp.left)

            if start == end:
                aa = []
                for i in sub:
                    aa.append(i.val)
                res.append(aa)

                if level % 2 == 0:
                    if len(q) == 0:
                        for i in stack:
                            if i.right != None:
                                q.append(i.right)
                            if i.left != None:
                                q.append(i.left)
                    bb = []
                    for i in stack[::-1]:
                        bb.append(i.val)
                    res.append(bb)

                sub = []
                stack = []
                start = 0
                end = len(q)
                level += 1
                
        return res


# if __name__ == '__main__':
#     t = TreeNode(1)
#     t.left = TreeNode(2)
#     t.right = TreeNode(3)
#     t.left.left = TreeNode(4)
#     t.right.right = TreeNode(5)
#     t.left.left.left = TreeNode(6)
#     t.right.right.right = TreeNode(7)
#     t.right.right.left = TreeNode(8)
#     for i in Solution().Print(t):
#         print i