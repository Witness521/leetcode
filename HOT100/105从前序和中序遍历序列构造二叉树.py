'''
给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历，
inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def mybuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中第一个节点就是根节点
            preorder_root = preorder_left
            # 中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 建立根节点
            root = TreeNode(preorder[preorder_root])
            # 左子树的节点数目
            left_tree_size = inorder_root - inorder_left
            root.left = mybuildTree(preorder_left + 1, preorder_left + left_tree_size,
                                    inorder_left, inorder_root - 1)
            root.right = mybuildTree(preorder_left + left_tree_size + 1, preorder_right,
                                     inorder_root + 1, inorder_right)

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        root = TreeNode(val=preorder[0])
        return mybuildTree(0, n-1, 0, n-1)


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归"""
        def recur_func(inorder):
            x = preorder.pop(0)
            node = TreeNode(x)
            # 中序遍历中的根节点
            idx = inorder.index(x)
            left_tree = inorder[:idx]
            right_tree = inorder[idx+1:]
            if left_tree:
                node.left = recur_func(left_tree)
            else:
                node.left = None

            if right_tree:
                node.right = recur_func(right_tree)
            else:
                node.right = None
            return node

        if not preorder or not inorder:
            return None
        return recur_func(inorder)

