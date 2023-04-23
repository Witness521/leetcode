'''
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], targetSum: int, currentSum: int):
            if not root.left and not root.right: # 左右子树都为空 是叶子节点
                if currentSum == targetSum:
                    return True
            if currentSum > targetSum:
                return False
            if root.left:
                left = dfs(root.left, targetSum, currentSum + root.left.val)
                if root.right:
                    right = dfs(root.right, targetSum, currentSum + root.right.val)
                return left or right

            if not root:
                return False
            return dfs(root, targetSum, root.val)