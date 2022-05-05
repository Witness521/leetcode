'''
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        if s is None:
            return t
        for i in s:
            if dict.get(i, None):
                dict[i] += 1
            else:
                dict[i] = 1
        for j in t:
            if dict.get(j, None):
                dict[j] -= 1
                if dict[j] < 0:
                    return j
            else:
                return j

if __name__ == '__main__':
    print(Solution().findTheDifference(s = "abcd", t = "abcde"))