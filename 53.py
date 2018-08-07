# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        
        queue = deque()
        stack = []
        queue.append(pRoot)
        stack.append(-1) # 注意这里，由于测试用例中有与根节点相同的val，所以这里设置为-1，避免根的val被栈弹出。
        
        while len(queue) > 0:
            elem = queue.popleft()
            if elem == None:
                continue
            else:
                queue.append(elem.left)
                if elem.left == None:
                    if elem.left == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(None)
                elif elem.left.val == stack[-1]:
                    stack.pop()
                else:
                    stack.append(elem.left.val)
                    
                queue.append(elem.right)
                if elem.right == None:
                    if elem.right == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(None)
                elif elem.right.val == stack[-1]:
                    stack.pop()
                else:
                    stack.append(elem.right.val)
                
        if len(stack) == 1:
            return True
        return False


# 借鉴了层次遍历的思想，使用Python额外的数据结构双端队列deque，栈中保存遍历的元素的值，如果有两个值相等就弹栈，最后留下根节点的值，个人认为比较好理解。