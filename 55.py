class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getCommonNode(self, path1, path2):
        min_iter_times = min(len(path1), len(path2))
        common_node = None

        for i in range(min_iter_times):
            if path1[i] == path2[i]:
                common_node = path1[i]

        return common_node

    # 这里的递归很难理解，记住，递归是一条一条路线走的
    def getNodePath(self, root, node, path):
        found = False
        path.append(root)

        if root.val == node.val:
            return True

        if not found and root.left != None:
            found = self.getNodePath(root.left, node, path)

        if not found and root.right != None:
            found = self.getNodePath(root.right, node, path)

        if not found:
            path.pop()
        return found


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

    path1 = []
    path2 = []

    s = Solution()
    s.getNodePath(a, a, path1)
    s.getNodePath(a, e, path2)

    common_node = s.getCommonNode(path1, path2)
    common_node_distance = path1.index(common_node) + 1
    
    print len(path1) + len(path2) - 2 * common_node_distance


# 参考：https://www.cnblogs.com/wxdjss/p/5698071.html