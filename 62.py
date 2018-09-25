class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def FindPath(self, root, expectNumber):
        res = []
        path = []
        self.helper(root, expectNumber, res, path)
        return res

    def helper(self, root, expectNumber, res, path):
        if root != None:
            path.append(root.val)
            
            if root.left == None and root.right == None:
                if sum(path) == expectNumber:
                    res.append(path[:])

            if root.left != None:
                self.helper(root.left, expectNumber, res, path)
            if root.right != None:
                self.helper(root.right, expectNumber, res, path)

            path.pop()


T = TreeNode(10)
T.left = TreeNode(5)
T.right = TreeNode(12)
T.left.left = TreeNode(4)
T.left.right = TreeNode(7)
print Solution().FindPath(T, 22)
