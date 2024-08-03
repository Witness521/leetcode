from typing import List



# 如果数组是单调递增或单调递减的，那么它是 单调 的。
#
# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。
#
# 当给定的数组 nums 是单调数组时返回 true，否则返回 false。
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        index = 0
        label = True
        # 考虑到一个元素和空的情况
        if len(nums) == 1 or len(nums) == 0:
            return True
        # 通过前两个的大小判断数组是递增还是递减
        # 如果前两个的大小一致，则向后比较
        while nums[index] == nums[index+1]:
            index += 1
            if index == len(nums)-1:
                return True
        if nums[index] < nums[index+1]:  # 递增
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        if nums[index] > nums[index+1]:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
        return label

'''
    没考虑到长度为1和0的情况
    没考虑到元素相等的情况
'''
