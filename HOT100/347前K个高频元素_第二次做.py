from typing import List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1
        min_heap = []
        for key, value in dict_num.items():
            if len(min_heap) >= k:
                # 判断堆顶最小元素和即将push元素的大小
                if min_heap[0][1] < value:
                    # min_heap.pop(0)  # 删除栈顶元素之后不能直接后一个元素顶上来
                    self.deleteMinHeap(min_heap)
                    self.push_heap(min_heap, (key, value))
            else:
                self.push_heap(min_heap, (key, value))
        return [i[0] for i in min_heap][::-1]

    def push_heap(self, tups: List[Tuple], tup: Tuple[int]):
        '''
            入堆的元素放在最后
        '''
        tups.append(tup)
        index = len(tups) - 1
        parent = (index - 1) // 2
        while index > 0 and tups[parent][1] > tups[index][1]:
            tups[index], tups[parent] = tups[parent], tups[index]
            index = parent
            parent = (index - 1) // 2

    def deleteMinHeap(self, min_heap: List[Tuple]):
        min_heap[0] = min_heap[-1]  # 最后一个元素放到堆顶
        min_heap.pop()
        def adjustDown(index: int, heap_end_index: int, min_heap: List[Tuple]):
            left = 2 * index + 1
            right = 2 * index + 2
            minIndex = index
            if left <= heap_end_index and min_heap[left][1] < min_heap[minIndex][1]:
                minIndex = left
            if right <= heap_end_index and min_heap[right][1] < min_heap[minIndex][1]:
                minIndex = right
            if minIndex == index:  # 最小值就是index
                return
            min_heap[minIndex], min_heap[index] = min_heap[index], min_heap[minIndex]
            adjustDown(minIndex, heap_end_index, min_heap)

        adjustDown(0, len(min_heap)-1, min_heap)




if __name__ == '__main__':
    print(Solution().topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6))