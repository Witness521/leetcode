# dp[i][j] 代表飞机从(i, j)到终点的最小耗费

def calcMinimumPower(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]

    dp[rows-1][cols-1] = max(1, 1 - grid[rows-1][cols-1])
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if i < rows - 1:
                dp[i][j] = max(1, dp[i+1][j] - grid[i][j])
            if j < cols - 1:
                dp[i][j] = max(1, dp[i][j+1] - grid[i][j])
    return dp[0][0]


m, n = list(map(int, input().split()))

grid = []
for grid_i in range(m):
    grid.append(list(map(int, input().split())))

res = calcMinimumPower(grid)
print(res)
