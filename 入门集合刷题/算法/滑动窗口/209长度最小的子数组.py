'''
给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        flag = 0
        min_len = float('inf')
        while left != right and right <= len(nums):
            length = right - left
            total = sum(nums[left:right])
            if total >= target and min_len > length:
                min_len = length
                flag = 1
            elif total < target:
                right += 1
            else:
                left += 1
        if flag:
            return min_len
        else:
            return 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
