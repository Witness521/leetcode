# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

class Solution:
    def __init__(self) -> None:
        self.result = []

    def combine(self, n: int, k: int, index: int, path: list):
        # 树的深度为k 宽度为1到9
        if len(path) == k and sum(path) == n:
            self.result.append(path.copy())
            return
        
        for i in range(index, 10):
            if len(path) >= k:  # 剪枝
                break
            path.append(i)
            self.combine(n, k, i + 1, path)
            path.pop()
        
if __name__ == '__main__':
    s = Solution()
    s.combine(5, 2, 1, [])
    print(s.result)