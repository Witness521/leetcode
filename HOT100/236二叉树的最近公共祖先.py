'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            left = self.lowestCommonAncestor(root.left, p, q)  # 左
            right = self.lowestCommonAncestor(root.right, p, q)  # 右
            if root.val == q.val or root.val == p.val:  # 这道题不用考虑abc中 b是不是c的父节点，往上传就可以了
                return root

            if left and right:
                return root
            if left == None and right != None:
                return right
            elif left != None and right == None:
                return left
            else:  # left == None and right == None
                return