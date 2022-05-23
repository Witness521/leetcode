'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
'''
from typing import List
import numpy as np


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 递推式 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        # 如果全是零才能返回零
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = np.zeros((len(matrix), len(matrix[0])))   # 代表正方形的右下角
        max_num = 0
        # 绘制左边框和上边框
        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0]
            if matrix[i][0]:
                max_num = 1
        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]
            if matrix[0][i]:
                max_num = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(int(dp[i-1][j-1]), int(dp[i-1][j]), int(dp[i][j-1])) + 1
                    if dp[i][j] > max_num:
                        max_num = dp[i][j]
        return int(max_num * max_num)

if __name__ == '__main__':
    print(Solution().maximalSquare([["1","0","1","0","0"],
                                    ["1","0","1","1","1"],
                                    ["1","1","1","1","1"],
                                    ["1","0","0","1","0"]]))