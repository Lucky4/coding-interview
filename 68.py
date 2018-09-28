# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_res = self.diameterOfBinaryTree(root.left)
        right_res = self.diameterOfBinaryTree(root.right)

        return max(left_res, right_res, self.get_path(root.left) + \
            self.get_path(root.right))
        
    def get_path(self, root):
        if root == None:
            return 0
        
        left = 1 + self.get_path(root.left)
        right = 1 + self.get_path(root.right)
        
        return max(left, right)