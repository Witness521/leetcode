'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0
    def rangeSumBST1(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return
        else:
            if low <= root.val <= high:
                self.total += root.val
        # 递归
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)

        return self.total

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        # 递归 加入剪枝
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # 符合查找的标准
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
