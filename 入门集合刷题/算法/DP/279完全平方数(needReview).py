'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

需要复习
'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            min_num = float("inf")
            for j in range(1, int(i**0.5)+1):
                min_num = min(dp[i - j * j], min_num)
            dp[i] = min_num + 1
        return dp[n]



if __name__ == '__main__':
    print(Solution().numSquares(13))