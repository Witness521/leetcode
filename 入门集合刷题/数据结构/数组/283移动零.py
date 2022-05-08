'''
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return []
        if nums == [0]:
            return [0]
        # 不需要双指针，只需要遍历一遍数组，把不为零的元素往前放就可以
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[index] = nums[i]
                index += 1
        # 将index后面的所有元素变成0
        for j in range(index, len(nums)):
            nums[j] = 0
        return nums



if __name__ == '__main__':
    print(Solution().moveZeroes([0,1,0,3,12]))