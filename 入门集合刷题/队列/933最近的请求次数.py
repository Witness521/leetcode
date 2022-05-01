# 写一个 RecentCounter 类来计算特定时间范围内最近的请求。
import collections
import queue


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return self.q.__len__()



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)