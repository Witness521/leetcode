# 最短的桥
import collections
from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 先通过bfs找到第一个岛屿中所有的节点
        for i in range(n):
            for j in range(n):
                islands = []
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        islands.append((x, y))
                        for nx, ny in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                q.append((nx, ny))
                                grid[nx][ny] = -1

                    # 每个节点都向外找一圈
                    step = 0
                    while True:
                        temp = islands
                        islands = []
                        for x, y in temp:
                            for nx, ny in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
                                if 0 <= nx < n and 0 <= ny < n:
                                    if grid[nx][ny] == 1:
                                        return step
                                    if grid[nx][ny] == 0:
                                        grid[nx][ny] = -1
                                        islands.append((nx, ny))
                        step += 1
                    return step

if __name__ == '__main__':
    print(Solution().shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))