"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间
"""
from typing import List

'''
    二分查找：通过count[i] <= i, 查找
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        l = 0
        r = length - 1
        count = 0
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            for i in nums:
                if i <= mid:
                    count = count + 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid  # 和正常二分查找的区别之处, 因为只有再让r往左移动的时候才是满足条件的情况, 此处记录的就是最后一次满足条件的mid
            count = 0
        return ans

if __name__ == '__main__':
    print(Solution().findDuplicate([1, 1]))