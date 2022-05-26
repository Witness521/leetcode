'''
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
'''
import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from functools import cmp_to_key
        dict = collections.defaultdict(int)
        item_list = []
        result = []
        for word in words:
            dict[word] += 1
        for item in dict.items():
            item_list.append(item)
        # item_list = sorted(item_list, key=lambda x: (-x[1], x[0]))  # sorted()默认正序排列，加-相当于是逆序
        print(item_list)
        item_list = sorted(item_list, key=cmp_to_key(self._compare))
        print(item_list)
        for i in range(k):
            result.append(item_list[i][0])
        return result

    def _compare(self, x, y):  # x在前，y在后，1就是换，-1不换
        if x[1] > y[1]:
            return -1  # 不换
        elif x[1] < y[1]:
            return 1  # 换
        else:
            if x[0] < y[0]:
                return -1
            else:
                return 1





if __name__ == '__main__':
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is"], k = 4))
