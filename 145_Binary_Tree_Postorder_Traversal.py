# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        ans = []
        def postorder(self, root):
            if root is None:
                return None
            if root.left != None:
                postorder(self, root.left)
            if root.right != None:
                postorder(self, root.right)
            ans.append(root.val)
        postorder(self, root)
        return ans


class Solution2:
    def postorderTraversal(self, root):
        ans = []
        if root is None:
            return ans
        stack = [root]
        while stack:
            root = stack.pop()
            ans.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        ans.reverse()
        return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution2().postorderTraversal(root)
    print(result)