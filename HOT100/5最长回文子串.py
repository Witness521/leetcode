'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''

import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) < 2:
        #     return s
        # # 动态规划
        # # 状态转移方程  dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        # dp = np.zeros((len(s), len(s)), dtype=bool)
        # maxLen = 1
        # begin = 0
        # # 初始化 所有长度为一的子串全都是回文串
        # for i in range(len(s)):
        #     dp[i][i] = True
        # # 先遍历字串长度
        # for L in range(2, len(s) + 1):
        #     # 枚举左边界
        #     for i in range(len(s)):
        #         # 右边界
        #         j = L + i - 1
        #         if j >= len(s):
        #             break
        #
        #         if s[i] != s[j]:
        #             dp[i][j] = False
        #         else:
        #             if j - i < 3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
        #         if dp[i][j] and j - i + 1 > maxLen:
        #             maxLen = j - i + 1
        #             begin = i
        # return s[begin:begin + maxLen]
        if len(s) < 2:
            return s
        n = len(s)
        begin = 0
        maxLen = 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True  # 对角线元素都为True
        for L in range(2, n+1):  # 先枚举字串长度
            for i in range(n):  # 枚举左边界
                j = i + L - 1  # 右边界
                if j < n:  # 如果右边界没有超出范围
                    if s[i] != s[j]:
                        dp[i][j] = False
                    else:
                        if j - i < 3:  # 如果字串长度为2
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i+1][j-1]
                else:
                    break

                if dp[i][j] and j - i + 1 > maxLen:
                    begin = i
                    maxLen = j - i + 1
        return s[begin : begin + maxLen]



if __name__ == '__main__':
    print(Solution().longestPalindrome('ac'))