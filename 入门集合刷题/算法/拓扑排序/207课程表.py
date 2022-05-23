'''
你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。

例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
'''
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        count = 0
        while node_queue:
            node = node_queue.popleft()
            count += 1
            for i in edges[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    node_queue.append(i)
        return count == numCourses


if __name__ == '__main__':
    print(Solution().canFinish(numCourses=4, prerequisites=[[2, 0], [2, 1], [3, 2]]))