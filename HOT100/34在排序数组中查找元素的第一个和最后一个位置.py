'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

你必须设计并实现时间复杂度为O(log n)的算法解决此问题
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return [-1, -1]
        # 二分查找
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                re_l, re_r = self.searchBiSide(nums, target, mid)
                return [re_l, re_r]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]

    def searchBiSide(self, nums: List[int], target: int, mid: int):
        l = mid
        r = mid
        while l >= 1 and nums[l - 1] == target:
            l -= 1

        while r + 1 < len(nums) and nums[r + 1] == target:
            r += 1

        return l, r

if __name__ == '__main__':
    print(Solution().searchRange(nums = [2, 2], target = 2))