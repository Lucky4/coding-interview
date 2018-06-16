# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        self.stack1.append(node)
        
        if len(self.stack2) == 0:
            self.stack2.append(node)
        elif node <= self.stack2[-1]:
            self.stack2.append(node)
        
    def pop(self):
        if self.stack1[-1] == self.stack2[-1]:
            self.stack2.pop()
        return self.stack1.pop()
    
    def top(self):
        return self.stack1[-1]
    
    def min(self):
        return self.stack2[-1]


# 这个题我一开始想的是在第二个栈中只保持一个最小元素，但是当第一个栈中有元素出栈的时候就会出现问题。
# 应该想到的是每当有元素进栈的时候，该元素出栈的时候是否影响第二个栈中的最小元素。
# 所以当有这种元素出现的时候，第二个栈中应该继续存储这种元素，然后当第一个栈该种元素出栈的时候，第二个栈也出栈。
