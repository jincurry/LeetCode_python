# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
# every node never differ by more than 1.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        try:
            self.getDepth(root)
        except:
            return False
        return True

    def getDepth(self, node):
        if node is None:
            return 0
        else:
            left_depth = self.getDepth(node.left)
            right_depth = self.getDepth(node.right)
            if abs(left_depth - right_depth) > 1:
                raise Exception
            return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    root = TreeNode(0)
    root.right = TreeNode(5)
    root.left = TreeNode(-10)
    root.left.right = TreeNode(-3)
    root.right.right = TreeNode(9)
    solution = Solution()
    print(solution.isBalanced(root))