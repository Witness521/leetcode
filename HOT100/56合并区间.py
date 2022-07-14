'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        # 先按照区间的左端点进行排序
        intervals.sort(key=lambda x: x[0])
        interval = intervals[0]
        for inter in intervals:
            # 两种情况
            # 如果右端点大于目前的区间右端点，并且左端点小于目前区间的右端点 则进行更新
            if inter[1] > interval[1] >= inter[0]:
                interval[1] = inter[1]
            elif interval[1] < inter[0]:
                result.append(interval)
                interval = inter
            else:
                continue
        result.append(interval)
        return result

if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,4],[4,5]]))
