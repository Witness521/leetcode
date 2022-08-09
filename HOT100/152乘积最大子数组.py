from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 用矩阵当作记录的方法超时
        # matrix = [[0] * len(nums) for _ in range(len(nums))]
        # max_res = max(nums)
        # # 对角线的值为对应元素值
        # for i in range(len(nums)):
        #     matrix[i][i] = nums[i]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         matrix[i][j] = matrix[i][j-1] * nums[j]
        #         if max_res < matrix[i][j]:
        #             max_res = matrix[i][j]
        # return max_res

        '''
            维护两个最大值和最小值数组
            最大值只会出现在最大的f*ai或者是最小的f*ai
        '''

        fmax = [-9999] * len(nums)
        fmin = [9999] * len(nums)
        fmax[0] = nums[0]
        fmin[0] = nums[0]
        for i in range(1, len(nums)):
            # dp递推式
            fmax[i] = max(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
            fmin[i] = min(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
        return max(max(fmax), max(fmin))



if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))
