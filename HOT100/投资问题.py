'''
    设有m元钱，n项投资，函数fi(x)表示将x元钱投入到第i项项目所产生的效益，i=1,…,n.问：如何分配这m元钱，使得投资的总效益最高？
'''
from typing import List


class Solution:
    def MaxProfit(self, f: List[List[int]], m: int, n: int):
        '''
            m元钱 n项投资
            dp[i][j]表示用 j 元投入到前 i 个项目中可以获取的最大收益；
            f[i][k]表示用 k 元投到第 i 个项目可以获取的收益；
            dp[i][j] = max(dp[i-1][j-k] + f[i][k], dp[i-1][j])
            时间复杂度O(nm^2)
        '''
        dp = [[0] * (m+1) for _ in range(n+1)]
        # 因为需要满足f(0)=0, 因此需要添加一行和一列
        f.insert(0, [0] * (m+1))
        for i in range(1, n+1):
            f[i].insert(0, 0)

        for i in range(n+1):
            for j in range(m+1):
                for k in range(1, j+1):
                    dp[i][j] = max(dp[i-1][j-k] + f[i][k], dp[i][j])
                dp[i][j] = max(dp[i][j], dp[i-1][j])
        print(dp)
        return dp[n][m]

if __name__ == '__main__':
    print(Solution().MaxProfit([
                                [11, 12, 13, 14, 15],
                                [0,  5,  10, 15, 20],
                                [2,  10, 30, 32, 40],
                                [20, 21, 22, 23, 24]
    ], 5, 4
    ))