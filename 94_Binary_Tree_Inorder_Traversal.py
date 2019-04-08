# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        ans = []
        def inorder(self, root):
            if root is None:
                return None
            if root.left != None:
                inorder(self, root.left)
            ans.append(root.val)
            if root.right != None:
                inorder(self, root.right)
        inorder(self, root)
        return ans


class Solution2:
    def inorderTraversal(self, root: TreeNode):
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution2().inorderTraversal(root)
    print(result)