'''
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            # 交换左右子树
            root.left, root.right = root.right, root.left
        if root is None:
            return root
        dfs(root)
        return root
