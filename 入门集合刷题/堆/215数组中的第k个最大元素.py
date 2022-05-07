'''给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。'''

'''使用大根堆'''
from typing import List


class Solution:
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

