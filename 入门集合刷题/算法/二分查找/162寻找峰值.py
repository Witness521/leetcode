'''峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。'''
from typing import List
'''二分法可以理解为上坡，上坡必有顶 因为nums[-1] = nums[n] = -∞ '''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 如果长度为一
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid + 1] < nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:  # 假如比两边全都小，使用右边
                left = mid + 1
        return left

