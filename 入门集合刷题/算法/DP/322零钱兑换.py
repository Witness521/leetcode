'''
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

    计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。

    你可以认为每种硬币的数量是无限的。
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 类似于背包问题，从0到amount设置一个list，存储最少到达amount的硬币数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] != float("inf"):
            return int(dp[amount])
        return -1




