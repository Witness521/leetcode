'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        # 使用动态规划的方法
        numsLen = len(nums)
        count = [0] * numsLen
        count[numsLen - 1] = 1
        if nums[-1] > nums[-2]:
            count[numsLen - 2] = 2
        else:
            count[numsLen - 2] = 1
        for i in range(numsLen-3, -1, -1):
            count = self.findMax(nums, count, i)
        result = max(count)
        return result


    def findMax(self, nums: List[int], count: List[int], begin):
        max = count[begin]
        for i in range(begin+1, len(nums)):
            if count[i] > max and nums[begin] < nums[i]:
                max = count[i]
        count[begin] = max + 1
        return count

if __name__ == '__main__':
    print(Solution().lengthOfLIS([0]))