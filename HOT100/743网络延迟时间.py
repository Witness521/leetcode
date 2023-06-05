'''
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
'''
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False] * n
        # 从i到j的距离 邻接矩阵
        g = [[float("inf")] * n for _ in range(n)]
        # 建图 邻接矩阵
        for source, target, weight in times:
            g[source-1][target-1] = weight
        # 从原点k到每个点的最近距离
        min_dist = [float("inf")] * n
        min_dist[k-1] = 0

        for _ in range(n):  # 循环n次
            flag = -1
            for i in range(n):
                # 找一个距离最近的点
                if not visited[i] and (flag == -1 or min_dist[i] < min_dist[flag]):
                    flag = i
            # 更新flag的值
            visited[flag] = True
            for i, dist in enumerate(g[flag]):
                if min_dist[i] > min_dist[flag] + dist:
                    min_dist[i] = min_dist[flag] + dist
        print(min_dist)
        result = max(min_dist)
        if result == float("inf"):
            return -1
        else:
            return result

if __name__ == '__main__':
    print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))