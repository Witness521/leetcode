'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法 本质是最远的位置的左边均可到达(纠正思想，并不是确定有最优解的题才能用贪心)
        if len(nums) == 1:
            return True
        far = 0  # 存储最远到达的位置
        for i in range(len(nums)-1):
            if far >= i:
                far = max(far, nums[i] + i)
            if far >= len(nums)-1:
                return True
        return False



        # DFS方法超时
        # def dfs(i: int, result: bool):
        #     if i == len(nums) - 1:
        #         return True
        #     if nums[i] == 0:
        #         result = False
        #     for j in range(1, nums[i]+1):
        #         result = dfs(i + j, result)
        #         if result:
        #             return True
        #     return False
        #
        # return dfs(0, False)

if __name__ == '__main__':
    print(Solution().canJump([3,0,8,2,0,0,1]))
