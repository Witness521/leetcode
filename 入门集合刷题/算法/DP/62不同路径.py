'''
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''
import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.zeros((m, n))
        # 描绘矩阵的上边框和左边框
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        i, j = 1, 1  # 行 列
        for i in range(1, m):
            j = 1
            while j < n:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                j += 1
        return int(dp[m-1][n-1])

if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
