"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
"""

class Solution:
    def reverse(self, x: int) -> int:
        n = 0; temp = 0
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)
        while x != 0:
            # 判断此时是否大于最大的32位整数
            if n > int_max // 10 or (n == int_max // 10 and temp > 7):
                return 0
            # 判断此时是否小于最大的32位整数
            if n < -(int_min // -10) or (n == -(int_min // -10) and temp < -8):
                return 0

            if x > 0:
                temp = x % 10
                x = x // 10
            else:
                temp = x % -10
                x = -(x // -10)

            n = n * 10 + temp
        return n

if __name__ == '__main__':
    print(Solution().reverse(-12))