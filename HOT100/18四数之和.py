# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        re = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                a = nums[i]
                b = nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if a + b - target == -(nums[left] + nums[right]) and [a, b, nums[left], nums[right]] not in re:
                        re.append([a, b, nums[left], nums[right]])
                        left += 1
                    else:
                        if a + b - target < -(nums[left] + nums[right]):
                            left += 1
                        else:
                            right -= 1
        return re

if __name__ == '__main__':
    print(Solution().fourSum([2,2,2,2,2]
,8))
