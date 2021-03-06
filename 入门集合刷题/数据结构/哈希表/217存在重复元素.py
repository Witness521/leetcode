'''给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        return False


