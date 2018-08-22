# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getCommonNode(self, root, node1, node2):
        if root == None:
            return None
        
        if root.val == node1.val or root.val == node2.val:
            return root

        L = self.getCommonNode(root.left, node1, node2)
        R = self.getCommonNode(root.right, node1, node2)

        if L != None and R != None:
            return root
        elif L != None and R == None:
            return L
        elif R != None and L == None:
            return R


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)

    a.left = b
    b.left = d
    d.left = None
    d.right = None
    b.right = e
    e.left = None
    e.right = None
    a.right = c
    c.right = g
    g.right = None
    g.left = None
    c.left = f
    f.left = None
    f.right = h
    h.left = None
    h.right = None
    #      a
    #     / \
    #    b   c
    #   / \ / \
    #  d  e f  g
    #        \
    #         h
    print Solution().getCommonNode(a, h, g).val