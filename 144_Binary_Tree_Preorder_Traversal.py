# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        ans = []
        
        def preorder(self, root):
            if root is None:
                return None
            ans.append(root.val)
            if root.left != None:
                preorder(self, root.left)
            if root.right != None:
                preorder(self, root.right)
        preorder(self, root)
        return ans


class Solution2:
    def preorderTraversal(self, root):
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                root = root.right
        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution2().preorderTraversal(root)
    print(result)


        