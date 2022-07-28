'''
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

    说明：

    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dict1 = {}
        # for num in nums:
        #     dict1[num] = dict1.get(num, 0) + 1
        # for item in dict1.items():
        #     if item[1] == 1:
        #         return item[0]

        # 方法二
        # 异或运算 满足交换律 a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b
        # 所以将所有的数字进行异或运算即可
        result = 0
        for num in nums:
            result = num ^ result
        return result

if __name__ == '__main__':
    print(Solution().singleNumber([0, 1, 1]))