"""
有 n 个城市通过一些航班连接。给你一个数组flights ，其中flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k站中转的路线，使得从 src 到 dst 的
价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。
"""
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 定义状态转移方程  dp[t][i] dp代表搭乘t次航班到达城市i的最小花费
        # dp[t][i] = min(dp[t-1][j] + cost(j, i))
        # 经过k站说明图中有2条边
        dp = [[float("inf")] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for t in range(1, k + 2):
            for i, j, cost in flights:
                dp[t][j] = min(dp[t-1][i] + cost, dp[t][j])
        # 逐行寻找到dst最小的cost
        min_cost = float("inf")
        for i in range(1, k+2):
            if dp[i][dst] < min_cost:
                min_cost = dp[i][dst]
        if min_cost == float("inf"):
            return -1
        return min_cost

if __name__ == '__main__':
    print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))