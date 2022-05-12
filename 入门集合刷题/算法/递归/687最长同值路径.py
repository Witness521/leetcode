'''
给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度由它们之间的边数表示。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        left = self.longestUnivaluePath1(root.left, 0)
        right = self.longestUnivaluePath(root.right, 0)
        return

    def findLong(self, root: TreeNode, length: int) -> int:
        if root is None:
            return length
        if root.left and root.val == root.left.val:
            left_len = self.findLong(root.left, length+1)
        else:
            left_len = self.findLong(root.left, 0)

        if root.right and root.val == root.right.val:
            right_len = self.findLong(root.right, length+1)
        else:
            right_len = self.findLong(root.right, 0)
        return left_len if left_len > right_len else right_len






