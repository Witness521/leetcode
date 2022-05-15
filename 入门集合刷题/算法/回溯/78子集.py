'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTracking(nums: List[int], startIndex: int, path: List[int]):
            self.result.append(path)
            # 结束的条件
            if startIndex >= len(nums):
                return

            for i in range(startIndex, len(nums)):
                backTracking(nums, i+1, path+[nums[i]])
        backTracking(nums, 0, [])
        return self.result


if __name__ == '__main__':
    print(Solution().subsets(nums=[1,2,3]))