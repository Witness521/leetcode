'''
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        f[i][j] 表示s的前i个字符和p中的前j个字符是否能够匹配，
        判断情况：
        1. s[i] == p[i]

        '''
        sLen = len(s)
        pLen = len(p)

        # 比较前i-1的s和j-1的p是否匹配
        def matches(i:int, j:int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (pLen + 1) for _ in range(sLen + 1)]
        f[0][0] = True
        for i in range(sLen + 1):
            for j in range(1, pLen + 1):
                if p[j-1] == '*':
                    f[i][j] = f[i][j] | f[i][j-2]
                    if matches(i, j-1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[sLen][pLen]

if __name__ == '__main__':
    print(Solution().isMatch("aa", "a"))

