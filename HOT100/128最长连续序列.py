'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为O(n) 的算法解决此问题。
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        # 去重
        num_set = set(nums)
        for num in num_set:
            # 如果num左边的元素不在num_set中
            # 不需要考虑左面的元素的原因是：如果这个元素有左侧的元素，那它一定不是最长的序列的左侧起始元素
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # 当num右边的元素在num_set中
                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num += 1

                longest = max(longest, current_streak)
        return longest



if __name__ == '__main__':
    print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))