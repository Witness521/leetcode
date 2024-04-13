from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums: List[int], left: int, right: int) -> List[int]:
        if left < right:
            x = nums[left]
            l = left + 1; r = right
            while l <= r:
                # 从左向右找第一个大于x的数
                while l <= r and nums[l] <= x:
                    l += 1
                # 从右向左找第一个小于x的数
                while l < r and nums[r] >= x:
                    r -= 1
                # 交换两个数的位置
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            # 将pivot放置在正确的位置
            nums[left], nums[r] = nums[r], nums[left]
            self.quickSort(nums, left, r-1)
            self.quickSort(nums, r+1, right)

if __name__ == '__main__':
    print(Solution().sortArray([2, 1, 5, 2, 0, 9]))