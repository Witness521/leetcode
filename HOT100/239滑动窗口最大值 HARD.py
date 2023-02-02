"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。
滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。
"""
import collections
from typing import List
# 方法：使用单调队列

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        hq = humdrum_queue()
        # 先将窗口中的数放进单调队列
        for i in range(k):
            hq.put(nums[i])
        # 将第一个窗口中的最大值放入
        result.append(hq.head)
        for i in range(k, len(nums)):
            hq.put(nums[i])
            hq.pop_(nums[i-k])
            result.append(hq.head)
        return result


class humdrum_queue:
    def __init__(self):
        self.queue = collections.deque()
        self.head = None

    def put(self, num):
        for i in range(len(self.queue) - 1, -1, -1):  # 从队尾进入单调队列
            if self.queue[i] < num:
                self.queue.pop()
                continue
            break
        if len(self.queue) == 0:
            self.head = num
        self.queue.append(num)

    def pop_(self, num):
        if self.head == num:
            self.queue.popleft()
            self.head = self.queue[0]

if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums = [1], k = 1))