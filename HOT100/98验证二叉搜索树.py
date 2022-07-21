'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:   # 这种方法未考虑右子树中所有节点和root的关系
        que = []
        que.append(root)
        while len(que) > 0:
            node = que.pop(0)
            if node.left and node.left.val >= node.val:
                return False
            else:
                if node.left:
                    que.append(node.left)

            if node.right and node.right.val <= node.val:
                return False
            else:
                if node.right:
                    que.append(node.right)
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 中序遍历即可完成
        def inOrder(root: Optional[TreeNode], orderList: list):
            if root is None:
                return
            inOrder(root.left, orderList)
            orderList.append(root.val)
            inOrder(root.right, orderList)
        orderList = []
        inOrder(root, orderList)
        for i in range(len(orderList)-1):
            if orderList[i] >= orderList[i+1]:
                return False
        return True

