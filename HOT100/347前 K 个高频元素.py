'''
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
'''
import heapq
from typing import List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        # 先进行计数
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1
            else:
                dict_num[num] = 1
        heap = []
        for num, freq in dict_num.items():
            self.push_heap(heap, (num, freq), k)  # 构建小根堆
            if len(heap) > k:
                heap.pop(0)

        res = []
        while heap:
            res.append(heap.pop()[0])
        return res[::-1]



    # 对小根堆进行调整
    def heapify(self, tup: Tuple[int], n: int, i: int):
        smallest = i  # 设置标定最小值
        # 层序遍历下的左右子树的index
        left = 2 * i + 1
        right = 2 * i + 2
        # 左子树比根结点小
        if left < n and tup[left][1] < tup[smallest][1]:
            smallest = left
        # 右子树比根节点大
        if right < n and tup[right][1] < tup[smallest][1]:
            smallest = right
        if i != smallest:
            tup[i], tup[smallest] = tup[smallest], tup[i]  # 交换
            self.heapify(tup, n, smallest)

    def build_heap(self, tup: List[Tuple]):
        n = len(tup)
        for i in range(n // 2 - 1, -1, -1):
            self.build_heap(tup)
        return tup

    # 构建最小堆
    # def push_heap(self, tups: List[Tuple], tup: Tuple):
    #     tups.append(tup)
    #     index = len(tups) - 1
    #     parent = (index - 1) // 2
    #     while index > 0 and tups[index][1] < tups[parent][1]:
    #         tups[index], tups[parent] = tups[parent], tups[index]
    #         index = parent
    #         parent = (index - 1) // 2

    def push_heap(self, tups: List[Tuple], tup: Tuple, k: int):
        if len(tups) == 0:
            tups.append(tup)
        elif len(tups) >= k:
            if tup[1] > tups[0][1]:
                tups.append(tup)
            else:
                return
        else:
            tups.append(tup)

        n = len(tups)
        self.heapify(tups, n, 0)


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6))