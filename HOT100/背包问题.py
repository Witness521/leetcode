'''
    一个旅行者随身携带一个背包,可以放入背包的物品有n种,每种物品的重量和价值分别是wi,vi,i=1,…,n
    如果背包的最大容量限制是b, 怎样选择放入背包的物品以使得背包的价值最大?
'''
from typing import List


class Solution:
    # def Knapsack_Problem(self, N: int, W: int, wt: List[int], val: List[int]):
    #     # dp[N][W] = totalVal  N是物品 W是空间 wt是每一个我物品所占的空间 val是每一个物品的价值
    #     # 完全背包状态转移方程  dp[i][v] = max{max(dp[i-1][v-k*wt[i]] + k*val[i]), dp[i-1][v]} 1 <= k <= v / wt[i]
    #     dp = [[0] * (W+1) for _ in range(N)]
    #     for i in range(N):  # 第几个物品
    #         for j in range(1, W+1):  # 空间大小
    #             for k in range(1, j // wt[i] + 1):
    #                 dp[i][j] = max(dp[i][j], dp[i-1][j-k*wt[i]] + k*val[i])  # 装k个第i个物品时候最大的值
    #             dp[i][j] = max(dp[i][j], dp[i-1][j])  # 对比一下装第i个物品的最大值和不装第i个物品的值谁大
    #     print('dp:', dp)
    #     return dp[N-1][W]

    def Knapsack_Problem(self, N: int, W: int, wt: List[int], val: List[int]):
        # dp[N][W] = totalVal  N是物品 W是空间 wt是每一个我物品所占的空间 val是每一个物品的价值
        # 完全背包状态转移方程  dp[i][v] = max{dp[i][v-wt[i]] + val[i], dp[i-1][v]}
        dp = [[0] * (W+1) for _ in range(N)]
        for i in range(N):  # 第几个物品
            for j in range(1, W+1):  # 空间大小
                if j - wt[i] >= 0:
                    dp[i][j] = max(dp[i][j-wt[i]] + val[i], dp[i-1][j])  # 完全背包的递推公式
                else:
                    dp[i][j] = dp[i-1][j]
        print('dp:', dp)
        return dp[N-1][W]



if __name__ == '__main__':
    print(Solution().Knapsack_Problem(N = 5, W = 8, wt = [8, 2, 3, 4, 5], val = [4, 2, 3, 5, 7]))
    # print(Solution().Knapsack_Problem(N=4, W=5, wt=[1, 2, 3, 5], val=[1, 4, 4, 7]))