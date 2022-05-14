'''
给定一个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority(left, right) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            # 左面找众数
            left_major = majority(left, mid)
            # 右面找众数
            right_major = majority(mid+1, right)

            if left_major == right_major:
                return left_major

            left_sum = sum(1 for i in nums[left:right+1] if i == left_major)
            right_sum = sum(1 for i in nums[left:right+1] if i == right_major)

            return left_major if left_sum > right_sum else right_major

        return majority(0, len(nums)-1)

if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))



