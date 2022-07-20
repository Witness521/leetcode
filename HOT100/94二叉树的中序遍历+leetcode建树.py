'''
    给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
'''

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTravel(root: Optional[TreeNode], result: List):
            if root is None:
                return
            inOrderTravel(root.left, result)
            result.append(root.val)
            inOrderTravel(root.right, result)

        result_list = []
        inOrderTravel(root, result=result_list)
        return result_list


"""
    leetcode中建树的方法
"""
def leetcodeCreateTree(valList: List):
    if len(valList) == 0:
        return None
    q = []
    # 设置一个标记判断是否需要填充左节点
    fill_left = True
    for val in valList:
        if val is not None:
            node = TreeNode(val)
        else:
            node = None
        if len(q) == 0:
            root = node
            q.append(node)
        elif fill_left:
            q[0].left = node
            fill_left = False
            if node:
                q.append(node)
        else:
            q[0].right = node
            q.pop(0)
            fill_left = True
            if node:
                q.append(node)
    return root



if __name__ == '__main__':
    root = leetcodeCreateTree([2, 4, None, 8])
    print(Solution().inorderTraversal(root))