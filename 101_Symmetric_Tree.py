# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        aStack = []
        aStack.append(root.left)
        aStack.append(root.right)

        while aStack:
            p = aStack.pop()
            q = aStack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            aStack.append(p.left)
            aStack.append(q.right)

            aStack.append(p.right)
            aStack.append(q.left)

        return True


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print(solution.isSymmetric(root))