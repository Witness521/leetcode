'''
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''
from typing import List


class Solution:
    def __init__(self):
        self.row = 0
        self.col = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)     # 行
        if self.row == 0:
            return 0
        self.col = len(grid[0])  # 列
        island_num = 0  # 岛屿数量
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == "1":
                    island_num += 1
                    grid = self.dfs(grid, i, j)
        return island_num

    # 目的是将此岛屿全都变成"0"
    def dfs(self, grid: List[List[str]], i, j):
        grid[i][j] = "0"
        if i+1 < self.row and grid[i+1][j] == "1":
            self.dfs(grid, i+1, j)
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.dfs(grid, i-1, j)
        if j+1 < self.col and grid[i][j+1] == "1":
            self.dfs(grid, i, j+1)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.dfs(grid, i, j-1)
        return grid






if __name__ == '__main__':
    print(Solution().numIslands([["1","1","1"],
                                 ["0","1","0"],
                                 ["1","1","1"]]
                                ))