'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1) + 1
        cols = len(word2) + 1
        # 由word1 转换到 word2 dp[i][j]代表从(i, j)到word1[i]到word2[j]需要操作的步数
        dp = [[0] * cols for _ in range(rows)]
        # 先对空行进行描边操作
        for j in range(cols):
            dp[0][j] = j

        for i in range(rows):
            dp[i][0] = i
        # 开始递推
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
        # 递推结束
        return dp[rows - 1][cols - 1]
    
















'''
    递归方法
'''
def minDistance(word1: str, word2: str) -> int:
    # 如果word1的长度为0 返回word2的长度 反之同理
    if len(word1) == 0 or len(word2) == 0:
        return max(len(word1), len(word2))
    if word1[-1] == word2[-1]:
        return minDistance(word1[:-1], word2[:-1])
    return min(minDistance(word1[:-1], word2), minDistance(word1, word2[:-1]), minDistance(word1[:-1], word2[:-1])) + 1


if __name__ == '__main__':
    print(minDistance("horse", "ros"))