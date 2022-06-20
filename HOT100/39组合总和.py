'''
给你一个 无重复元素 的整数数组candidates 和一个目标整数target，
找出candidates中可以使数字和为目标数target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为target 的不同组合数少于 150 个。
'''
from typing import List


class Solution:
    def __init__(self):
        self.total_result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 此题不是背包问题，因为每一个数字无限量 因此需要用回溯解
        def dfs(candidates: List[int], target: int, result: List[int], total: int, begin):
            if total == target:
                self.total_result.append(list(result))
            for i in range(begin, len(candidates)):
                if total + i <= target:
                    result.append(candidates[i])
                    dfs(candidates, target, result, total + candidates[i], i)
                    result.pop()

        dfs(candidates, target, [], 0, 0)

        return self.total_result

if __name__ == '__main__':
    print(Solution().combinationSum([2,7,6,3,5,1], 9))