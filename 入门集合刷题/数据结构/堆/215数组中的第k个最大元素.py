'''给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。'''

'''使用大根堆'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            通过删除k次堆顶元素，第k次获得的就是第k大的元素
        '''
        heapSize = len(nums)
        self.build_minHeap(nums, k)
        for i in range(k, heapSize):
            # 如果待添加的元素大于堆顶元素则将其入堆
            if nums[i] > nums[0]:
                nums[0], nums[i] = nums[i], nums[0]
                # 只需要将堆顶重新进行调整即可
                self.adjust_minHeap(nums, k, 0)

        return nums[0]

    def build_minHeap(self, nums: List[int], k: int):
        # 从最后一个非叶子节点开始进行建大根堆
        for i in range(k // 2 - 1, -1, -1):
            self.adjust_minHeap(nums, k, i)

    # 使用前k个元素建立小根堆
    def adjust_minHeap(self, nums: List[int], k: int, i: int):
        min_pos = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < k and nums[min_pos] > nums[left]:
            min_pos = left
        if right < k and nums[min_pos] > nums[right]:
            min_pos = right
        if i != min_pos:
            nums[i], nums[min_pos] = nums[min_pos], nums[i]
            self.adjust_minHeap(nums, k, min_pos)

'''
    大根堆 目前Leetcode最后一组测试数据超时
'''
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            self.build_maxheap(nums)
            result = nums.pop(0)
        return result


    def build_maxheap(self, nums: List[int]):
        heapSize = len(nums)
        for i in range((heapSize-2) // 2, -1, -1):
            self.adjust_heap(nums, i, heapSize)

    def adjust_heap(self, nums: List[int], i:int, heapSize:int):
        left = i * 2 + 1
        right = i * 2 + 2
        max = i
        # 如果左儿子节点在list中，并且左儿子大于max指针所指
        if left < heapSize and nums[left] > nums[max]:
            max = left
        if right < heapSize and nums[right] > nums[max]:
            max = right
        if max != i:
            # max和i进行交换
            nums[max], nums[i] = nums[i], nums[max]
            # 由于交换了父节点和子节点，因此可能对子节点的子树造成影响，所以对子树进行调整
            # 递归调用，从交换后的树继续向下搜素
            self.adjust_heap(nums, max, heapSize)

if __name__ == '__main__':
    print(Solution().findKthLargest([-1,2,0], 2))

