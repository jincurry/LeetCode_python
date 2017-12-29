# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(-10)
    root.right = TreeNode(5)
    root.left.left = TreeNode(21)
    root.left.right = TreeNode(24)
    root.right.right = TreeNode(9)
    solution = Solution()
    print(solution.minDepth(root))