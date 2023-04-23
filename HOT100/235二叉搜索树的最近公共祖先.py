'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 此题可以用分治做
        # 根节点的值在p和q之间
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        # 如果p和q都在root的左边
        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor(root.left, p, q)
        # 如果p和q都在root的右边
        if p.val > root.val and q.val > root.val:  # 如果p和q都在root的左边
            self.lowestCommonAncestor(root.right, p, q)