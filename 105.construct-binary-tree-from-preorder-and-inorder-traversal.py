#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        splitPoint = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:splitPoint+1], inorder[:splitPoint])
        root.right = self.buildTree(preorder[splitPoint+1:], inorder[splitPoint+1:])
        return root

