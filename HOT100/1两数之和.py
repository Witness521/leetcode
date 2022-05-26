'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''
import collections
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = collections.defaultdict(int)  # 使用hash表
        # for num in nums:
        #     dict1[num] += 1
        # result = []
        # for num in nums:
        #     left = target - num
        #     if left == num:
        #         if dict1[num] >= 2:
        #             for i in range(len(nums)):
        #                 if nums[i] == left and i not in result:
        #                     result.append(i)
        #                 if nums[i] == num and i not in result:
        #                     result.append(i)
        #         else:
        #             continue
        #     elif dict1[left] >= 1 and (dict1[num] - 1) >= 0:
        #         # 找到了
        #         for i in range(len(nums)):
        #             if nums[i] == left and i not in result:
        #                 result.append(i)
        #             if nums[i] == num and i not in result:
        #                 result.append(i)
        #         break
        # return result
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target-num]]
            dict[num] = i




if __name__ == '__main__':
    print(Solution().twoSum([3,2,4], 6))




