'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''

import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        # 状态转移方程  dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = np.zeros((len(s), len(s)), dtype=bool)
        maxLen = 1
        begin = 0
        # 初始化 所有长度为一的子串全都是回文串
        for i in range(len(s)):
            dp[i][i] = True
        # 先遍历字串长度
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    begin = i
        print(dp)
        return s[begin:begin + maxLen]

if __name__ == '__main__':
    print(Solution().longestPalindrome('abbc'))