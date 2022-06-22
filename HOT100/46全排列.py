'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''
from typing import List

# 回溯的问题
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], re: List[int], total_list: List[int]):
            if len(re) == len(nums):
                total_list.append(list(re))
                return
            for i in nums:
                if i not in re:
                    re.append(i)
                    dfs(nums, re, total_list)
                    re.pop()
        total_list = []
        dfs(nums, [], total_list)
        return total_list

if __name__ == '__main__':
    print(Solution().permute([1, 2]))

