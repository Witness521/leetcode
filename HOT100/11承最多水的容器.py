'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''

# 采用的是双指针
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针，两边开始向内侧移动，移动小的那边的
        left = 0
        right = len(height) - 1
        maxArea = (right - left) * min(height[left], height[right])
        while left < right:
            maxArea = max((right - left) * min(height[left], height[right]), maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
