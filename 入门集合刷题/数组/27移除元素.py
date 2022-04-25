'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return []
        index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[index] = nums[i]
                index += 1
        # 将index后面的所有元素变成0
        for j in range(index, len(nums)):
            nums[j] = val
        return index, nums

if __name__ == '__main__':
    print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))