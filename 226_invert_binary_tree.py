# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            nodes = []
            nodes.append(root)
            while nodes:
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
        return root


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(7)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(6)
    f = TreeNode(9)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    answer = solution.invertTree(root)
    print(answer.val, answer.left.val, answer.right.val)
    print(answer.left.left.val, answer.left.right.val)
    print(answer.right.left.val, answer.right.right.val)

