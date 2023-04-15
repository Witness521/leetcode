"""
    给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

    一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
    两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            最难的就是确定dp的意义：dp[i][j]  text1中从0到i 和 text2中从0到j的最大公共子序列的长度
        '''
        m = len(text1) + 1
        n = len(text2) + 1
        # 构建一个m行n列的数组
        dp = [[0] * (n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:  # text1 和 text2 索引是从0开始的
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 此步骤可以从图中得来，二维数组从上和左推得
        return dp[m-1][n-1]