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

        # 不满足最优子结构 因为出现负数的时候负数小于正数，但又无法判断后面是否还有负数
        '''
            分情况进行讨论
            1. 如果第i个位置的数是正数的话 那么希望其前一个位置结尾的某个段的积也是正数 并尽可能大
            2. 如果第i个位置的数是负数的话 那么希望其前一个位置结尾的某个段的积也是负数 并尽可能小
            fmax(i) = max{a_i * fmax(i-1), a_i * f_min(i-1), a_i}
            fmin(i) = min{a_i * fmax(i-1), a_i * f_min(i-1), a_i}
        '''
        fmax = [nums[0]] * len(nums)
        fmin = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            fmax[i] = max(nums[i] * fmax[i-1], nums[i] * fmin[i-1], nums[i])
            fmin[i] = min(nums[i] * fmax[i-1], nums[i] * fmin[i-1], nums[i])
        return max(fmax)

if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))
