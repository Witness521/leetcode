'''给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，
写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

有序数组
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums: List[int], target: int, left:int, right:int):
        if left > right:
            return -1
        mid = (left+right) // 2  # 计算出mid
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right)
        else:
            return self.binarySearch(nums, target, left, mid-1)

if __name__ == '__main__':
    print(Solution().search([-1,0,3,5,9,12], 9))


