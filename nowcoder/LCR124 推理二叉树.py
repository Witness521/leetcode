
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inferTree(self, preOrder, inOrder:list):
        
        def dfs(preOrder, inOrder:list):
            if preOrder == []:
                return None
            root = preOrder.pop()
            idx = inOrder.index(root)
            node = TreeNode(root)
            left = inOrder[:idx]
            right = inOrder[idx+1:]
            node.left = dfs(preOrder, left)
            node.right = dfs(preOrder, right)
            return node

        return dfs(preOrder, inOrder)

