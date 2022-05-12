'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_len = 0

    def searchDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left_depth = self.searchDepth(root.left)
        right_depth = self.searchDepth(root.right)
        if left_depth + right_depth > self.max_len:
            self.max_len = left_depth + right_depth
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.searchDepth(root)
        return self.max_len