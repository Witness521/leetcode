'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
'''
from typing import List


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     row = len(grid)
    #     col = len(grid[0])
    #     result_list = []
    #     def dfs(i:int, j:int, total:int):
    #         if i == row-1 and j == col-1:
    #             return total + grid[row-1][col-1]
    #         # 向右
    #         if j < col-1:
    #             to_right = dfs(i, j+1, total + grid[i][j])
    #             result_list.append(to_right)
    #         # 向下
    #         if i < row-1:
    #             to_down = dfs(i + 1, j, total + grid[i][j])
    #             result_list.append(to_down)
    #         return min(result_list)
    #     return dfs(0, 0, 0)

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     if not grid or not grid[0]:
    #         return 0
    #     row = len(grid)
    #     col = len(grid[0])
    #     cost = [[0] * col for _ in range(row)]
    #     # 描边
    #     cost[0][0] = grid[0][0]
    #     for i in range(1, row):
    #         cost[i][0] = cost[i-1][0] + grid[i][0]
    #     for j in range(1, col):
    #         cost[0][j] = cost[0][j - 1] + grid[0][j]
    #     for i in range(1, row):
    #         for j in range(1, col):
    #             cost[i][j] = min(cost[i-1][j] + grid[i][j], cost[i][j-1] + grid[i][j])
    #     return cost[row-1][col-1]
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 设置一个路径长度的矩阵
        m = len(grid)
        n = len(grid[0])
        cost_matrix = [[0] * n for _ in range(m)]
        # 首先进行描边操作
        total_cost = 0
        for i in range(n):
            total_cost += grid[0][i]
            cost_matrix[0][i] = total_cost
        total_cost = 0
        for i in range(m):
            total_cost += grid[i][0]
            cost_matrix[i][0] = total_cost
        # 递推公式 cost_matrix[i][j] = min(cost_matrix[i-1][j], cost_matrix[i][j-1]) + grid[i][j]
        for i in range(1, m):
            for j in range(1, n):
                cost_matrix[i][j] = min(cost_matrix[i-1][j], cost_matrix[i][j-1]) + grid[i][j]
        return cost_matrix[m-1][n-1]



if __name__ == '__main__':
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))