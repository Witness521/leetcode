'''
    给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left: TreeNode, right: TreeNode):
            # 左右都是None
            if not left and not right:
                return True
            # 左右只有一个为None
            if not (left and right) and (left or right):
                return False
            # 左右两个都不为None
            if left.val == right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else:
                return False
        if root is None:
            return True
        check(root.left, root.right)




    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        # 左子树
        left_tree = root.left
        # 右子树
        right_tree = root.right
        if left_tree == right_tree is None:
            return True

        def dfs_left(root: Optional[TreeNode], llist: list):
            if root is None:
                llist.append(None)
                return
            dfs_left(root.left, llist)
            llist.append(root.val)
            dfs_left(root.right, llist)

        def dfs_right(root: Optional[TreeNode], rlist: list):
            if root is None:
                rlist.append(None)
                return
            dfs_right(root.right, rlist)
            rlist.append(root.val)
            dfs_right(root.left, rlist)

        llist = []
        rlist = []
        dfs_left(left_tree, llist)
        dfs_right(right_tree, rlist)
        if llist == rlist:
            return True
        else:
            return False
