'''
    给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
        输入：nums = [1,0,1,1,0,1]
        输出：2
'''
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 判断nums是否为空
        if nums is None:
            return 0
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
        return max_count
