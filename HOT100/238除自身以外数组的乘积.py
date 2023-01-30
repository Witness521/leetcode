'''
给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。

题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。

请不要使用除法，且在O(n) 时间复杂度内完成此题。
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 先求左半部分的乘积
        left_product = [1] * len(nums)
        right_prodect = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = nums[i-1] * left_product[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_prodect[i] = nums[i+1] * right_prodect[i+1]
        for i in range(len(nums)):
            result[i] = left_product[i] * right_prodect[i]
        return result


if __name__ == '__main__':
    Solution().productExceptSelf([1, 2, 3, 4])