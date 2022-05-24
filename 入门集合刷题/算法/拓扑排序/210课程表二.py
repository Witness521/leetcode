'''
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
'''
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        node_queue = collections.deque()
        # 每一个节点的入度
        in_degree = [0] * (numCourses)
        for course_list in prerequisites:
            edges[course_list[1]].append(course_list[0])  # 字典中的键是课程，值是依赖这门课的后续课
            in_degree[course_list[0]] += 1
        # 添加入度为零的节点
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                node_queue.append(i)
        learn_order = []
        while node_queue:
            node = node_queue.popleft()
            learn_order.append(node)
            for i in edges[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    node_queue.append(i)
        if len(learn_order) < numCourses:
            return []
        else:
            return learn_order