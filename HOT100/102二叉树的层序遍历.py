'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''

# Definition for a binary tree node.
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 使用队列完成层序遍历
        que = collections.deque()
        result = []
        if not root:
            return result
        que.append(root)
        while que:
            size = len(que)
            re = []
            for i in range(size):
                node = que.popleft()
                if node:
                    re.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            result.append(re)
        return result