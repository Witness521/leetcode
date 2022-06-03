'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''
import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 遍历每一个数，然后将三数之和问题变成两数之和的问题
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            left_num = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] < left_num:
                    left += 1
                elif nums[left] + nums[right] > left_num:
                    right -= 1
                else:
                    three = [nums[i], nums[left], nums[right]]
                    three.sort()
                    if three not in result:
                        result.append(three)
                    left += 1
                    right -= 1
        return result

if __name__ == '__main__':
    print(Solution().threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]))

