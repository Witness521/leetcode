'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root in ([], None):
            return True
        elif abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
            # return True  # 这样写相当于只判断根节点是否是平衡二叉树

    # 计算高度
    def height(self, root: TreeNode):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

if __name__ == '__main__':
    Solution().isBalanced([])