'''
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。这里的 i - 1 和 i + 1 代表
和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

Hard
'''
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        # 将nums首尾添1
        nums.append(1)
        nums.insert(0, 1)
        # dp[i][j]代表从i到j戳气球获得的最大硬币数量
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for l in range(1, length+1):
            for i in range(1, length-l+2):
                j = i + l - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1])
        return dp[1][length]