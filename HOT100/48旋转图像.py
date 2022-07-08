'''
给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先对角翻一下 再顺时针向右翻一下
        n = len(matrix)
        for i in range(1, n):
            for j in range(0, i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        axis = n // 2
        for i in range(axis):
            for j in range(n):
                matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]

        return matrix


if __name__ == '__main__':
    print(Solution().rotate([[1]]))