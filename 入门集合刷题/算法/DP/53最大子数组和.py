'''
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    子数组 是数组中的一个连续部分。
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

if __name__ == '__main__':
    print(Solution().maxSubArray([5,4,-1,7,8]))
