# 二叉排序树 求第k小的值

class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findK(self, root, k):
        result = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        print(result[k-1])

if __name__ == '__main__':
    node1 = TreeNode(val=1)
    node4 = TreeNode(val=4)
    node3 = TreeNode(val=3)
    node3.left = node1
    node3.right = node4
    Solution().findK(node3, 1)
        

            



