'''
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。
'''
class Solution:
    # def maxVowels(self, s: str, k: int) -> int:
    #     # 这种写法超时
    #     if s == '' or k == 0:
    #         return 0
    #     yuanyin = ['a', 'e', 'i', 'o', 'u']
    #     max_len = 0
    #     left = 0
    #     right = k
    #     while right <= len(s):
    #         string_temp = s[left:right]
    #         length = 0
    #         for i in string_temp:
    #             if i in yuanyin:
    #                 length += 1
    #                 if length > max_len:
    #                     max_len = length
    #         left+=1
    #         right+=1
    #     return max_len

    def maxVowels(self, s: str, k: int) -> int:
        # 这种写法超时
        if s == '' or k == 0:
            return 0
        yuanyin = ['a', 'e', 'i', 'o', 'u']
        max_len = 0
        left = 0
        right = k
        string_temp = s[left:right]
        length = 0
        for i in string_temp:
            if i in yuanyin:
                length += 1
                max_len = length
        while right < len(s):
            # 滑动窗口的三种情况
            # 1. 滑入元音，滑出原音  不改变
            # 2. 滑入元音，滑出非元音 +1
            # 3. 滑入非元音，滑出元音 -1
            length = length - self.isVowel(s[left]) + self.isVowel(s[right])
            if length > max_len:
                max_len = length
            left += 1
            right += 1
        return max_len

    def isVowel(self, ch) -> int:
        return int(ch in "aeiou")

if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef" ,3))