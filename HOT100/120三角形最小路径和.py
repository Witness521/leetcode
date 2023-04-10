'''
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # if len(triangle) == 1:
        #     return triangle[0][0]
        # m = len(triangle[len(triangle) - 1])  # 树最后一层的大小
        # total_cost = [[10000] * m for _ in range(m)]
        # total_cost[0][0] = triangle[0][0]
        # for i in range(1, m):
        #     for j in range(i + 1):
        #         if j == 0:
        #             total_cost[i][j] = total_cost[i-1][j] + triangle[i][j]
        #         total_cost[i][j] = min(total_cost[i-1][j-1], total_cost[i-1][j]) + triangle[i][j]
        # min_val = 10000
        # for i in range(m):
        #     if total_cost[m-1][i] < min_val:
        #         min_val = total_cost[m-1][i]
        # return min_val


        # 第二种方法 自底向上的方法，在原数组的基础上进行修改
        if len(triangle) == 1:
            return triangle[0][0]
        m = len(triangle[len(triangle) - 1])  # 树最后一层的大小
        for i in range(m-2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]



if __name__ == '__main__':
    print(Solution().minimumTotal([[-1],[-2,-3]]))