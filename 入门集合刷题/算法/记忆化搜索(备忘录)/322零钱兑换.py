'''
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

    计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。

    你可以认为每种硬币的数量是无限的。

    记忆化搜索(备忘录)：
        实则为DFS遍历或BFS遍历的升级版，只是将重复计算的部分进行记录减少计算，即：备忘录DFS
'''
from typing import List


class Solution:
    def __init__(self):
        self.min_total = float("inf")
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0] * (amount + 1)
        def dfs(rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if memo[rem]:
                return memo[rem]
            # 这个result的位置决定是否算对
            # result代表的是此rem对应的
            result = float("inf")
            for coin in coins:
                count = dfs(rem - coin, count+1)  # 得到硬币的数量
                if count == -1: continue
                result = min(result, count+1)
            memo[rem] = result if result != float("inf") else -1
            return memo[rem]

        if amount == 0:
            return 0
        return dfs(amount, 0)

if __name__ == '__main__':
    print(Solution().coinChange([5, 2, 1], 11))