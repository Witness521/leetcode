'''
    给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
'''
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        # m 行 n 列
        m = len(matrix)
        n = len(matrix[0])
        # dp数组代表当前列从上到下最大的矩形
        dp = [[0] * n for _ in range(m)]
        # 描边 描第一行
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = 0
        area = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0: continue
                curHeight = dp[i][j]
                for k in range(j, -1, -1):
                    if dp[i][k] == 0:
                        break
                    curWidth = j - k + 1
                    curHeight = min(curHeight, dp[i][k])
                    area = max(area, curHeight * curWidth)
        return area

if __name__ == '__main__':
    print(Solution().maximalRectangle([["1"]]))