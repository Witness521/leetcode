'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        if digits[length - 1] != 9:  # 如果最后一位不是9
            digits[length - 1] += 1
            return digits

        n = length - 1
        while digits[n] == 9 and n >= 0:  # 找到从末尾开始第一个不为9的元素
            digits[n] = 0
            n -= 1
        if n < 0:  # 所有数字全是9, 需要在第一位添加1
            digits.insert(0, 1)
        else:  # 在第一个不为9的位置加一
            digits[n] += 1

        return digits

if __name__ == '__main__':
    print(Solution().plusOne(digits = [0]))