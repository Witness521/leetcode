'''
给定一个包含红色、白色和蓝色、共n 个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。
'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left = 0
        # right = len(nums) - 1
        # cur = 0
        # while cur <= right:
        #     if nums[cur] == 0:
        #         nums[cur], nums[left] = nums[left], nums[cur]
        #         left += 1
        #     elif nums[cur] == 2:
        #         nums[cur], nums[right] = nums[right], nums[cur]
        #         right -= 1
        #     cur += 1
        # print(nums)

        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            if i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
        print(nums)


if __name__ == '__main__':
    Solution().sortColors(nums = [1,2,0])