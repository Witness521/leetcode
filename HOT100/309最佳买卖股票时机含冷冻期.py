'''
给定一个整数数组prices，其中第prices[i]表示第i天的股票价格

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        # f = [[0, 0, 0]] * days  不能这么写的原因是：python会自动引用 导致修改一个全都改变
        f = [[-prices[0], 0, 0]] + [[0, 0, 0] for i in range(days - 1)]
        # f[0][0] = -prices[0]  # 持有
        # f[0][1] = 0  # 冷冻期
        # f[0][2] = 0  # 不持有 不冷冻
        for i in range(1, days):
            f[i][0] = max(f[i-1][0], f[i-1][2] - prices[i])
            f[i][1] = f[i-1][0] + prices[i]
            f[i][2] = max(f[i-1][1], f[i-1][2])
        return max(f[days-1][0], f[days-1][1], f[days-1][2])

if __name__ == '__main__':
    print(Solution().maxProfit(prices = [1,2,3,0,2]))

