'''
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。
'''
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[len(cost) - 1]

if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))