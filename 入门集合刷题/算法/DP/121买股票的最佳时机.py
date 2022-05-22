'''
给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] - min_num > maxProfit:
                maxProfit = prices[i] - min_num
            if prices[i] < min_num:
                min_num = prices[i]
        return maxProfit


if __name__ == '__main__':
    print(Solution().maxProfit([7,6,4,3,1]))