'''
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。
[
[1,1,0],
[1,1,0],
[0,0,1]
]
'''
import collections
from typing import List


class Solution:
    # 并查集
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 查找index的父节点
        def find(index: int):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        # 将i合并到j的集合中
        def union(i: int, j: int):
            parent[find(i)] = find(j)

        cities = len(isConnected)
        parent = list(range(cities))

        for i in range(cities):
            for j in range(i+1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)

        total_num = 0
        for k in range(cities):
            if parent[k] == k:
                total_num += 1
        return total_num



if __name__ == '__main__':
    print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))