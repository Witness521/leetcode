'''
给定n个矩阵：A1,A2,...,An，其中Ai与Ai+1是可乘的，i=1，2...，n-1。
确定计算矩阵连乘积的计算次序，使得依此次序计算矩阵连乘积需要的数乘次数最少。
'''

# 使用动态规划的思想
from typing import List


def Matrix_chain_Order(p: List[int], n:int):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    # 递推公式  m[i][j] = min{m[i][k]+m[k+1][j]+pi-1*pk*pj}  i < j; i <= k <= j-1
    for L in range(2, n+1):  # 从长度为2开始遍历
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = -1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]   # 递推公式
                if q < m[i][j] or m[i][j] == -1:
                    m[i][j] = q
    return m[0][n-1]

if __name__ == '__main__':
    print(Matrix_chain_Order([10, 100, 5, 50], 3))
