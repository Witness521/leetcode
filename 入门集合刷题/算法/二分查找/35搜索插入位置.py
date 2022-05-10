'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)
    def binarySearch(self, nums: List[int], target: int, left:int, right:int):
        if left <= right:
            mid = (left + right) // 2  # 计算出mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binarySearch(nums, target, mid + 1, right)
            else:
                return self.binarySearch(nums, target, left, mid - 1)
        else:
            return left  # 如果没找到，左右指针相邻，左指针指向最大小于target的值，右指针指向最小大于target的值


if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 4))
