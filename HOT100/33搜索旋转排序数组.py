'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

你必须设计一个时间复杂度为O(log n)的算法解决此问题。
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:  # 左侧有序
                if nums[l] <= target <= nums[mid]:  # 并且target在左侧中
                    return self.binarySearch(l, mid-1, nums, target)
                else:  # target不在左侧中
                    l = mid + 1
            else:  # 右侧有序
                if nums[mid] <= target <= nums[r]:  # 并且target在右侧中
                    return self.binarySearch(mid+1, r, nums, target)
                else:  # target不在右侧中
                    r = mid - 1
        return -1

    def binarySearch(self, l, r, nums, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

if __name__ == '__main__':
    print(Solution().search([3, 1], 1))
