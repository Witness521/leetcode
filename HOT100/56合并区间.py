'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # result = []
        # # 先按照区间的左端点进行排序
        # intervals.sort(key=lambda x: x[0])
        # interval = intervals[0]
        # for inter in intervals:
        #     # 两种情况
        #     # 如果右端点大于目前的区间右端点，并且左端点小于目前区间的右端点 则进行更新
        #     if inter[1] > interval[1] >= inter[0]:
        #         interval[1] = inter[1]
        #     elif interval[1] < inter[0]:
        #         result.append(interval)
        #         interval = inter
        #     else:
        #         continue
        # result.append(interval)
        # return result
        result = []
        # 按照intervals的第一个元素进行排序
        intervals.sort(key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        for inter in intervals:
            if inter[1] > right >= inter[0]:
                right = inter[1]  # 更新right
            elif right < inter[0]:
                result.append([left, right])
                left = inter[0]
                right = inter[1]
            else:
                continue
        result.append([left, right])
        return result

if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,4],[6,7],[9,10]]))
