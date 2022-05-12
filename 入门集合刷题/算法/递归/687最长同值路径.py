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
    def __init__(self):
        self.max_len = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def search(root: TreeNode):
            if root is None:
                return 0
            left_depth = search(root.left)
            right_depth = search(root.right)
            if root.left and root.right and root.left.val == root.val == root.right.val:
                self.max_len = max(self.max_len, left_depth + right_depth + 2)
                return max(left_depth, right_depth) + 1
            elif root.left and root.val == root.left.val:
                self.max_len = max(self.max_len, left_depth + 1)
                return left_depth + 1
            elif root.right and root.val == root.right.val:
                self.max_len = max(self.max_len, right_depth + 1)
                return right_depth + 1
            else:
                return 0
        search(root)
        return self.max_len





