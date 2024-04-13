'''
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # 此题为滑动窗口  典型！！！
    #     # left = 0
    #     # right = 0
    #     # max_len = 0
    #     # currentLen = 0
    #     # hashset = set()
    #     # while right < len(s):
    #     #     while s[right] in hashset:
    #     #         hashset.remove(s[left])
    #     #         left += 1
    #     #         currentLen -= 1
    #     #     hashset.add(s[right])
    #     #     right += 1
    #     #     currentLen += 1
    #     #     max_len = max(max_len, currentLen)
    #     # return max_len

    #     left = 0  # 左指针
    #     right = 0  # 右指针
    #     curentLen = 0
    #     maxLen = 0
    #     hashset = set()
    #     while right < len(s):
    #         if s[right] not in hashset:
    #             hashset.add(s[right])
    #             right += 1
    #             curentLen += 1
    #             if curentLen > maxLen:
    #                 maxLen = curentLen
    #         else:
    #             hashset.remove(s[left])
    #             left += 1
    #             curentLen -= 1
    #     return maxLen

    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        max_length = 0
        # 滑动窗口的思想
        left = 0
        right = 0
        while right < len(s) and left < len(s):
            c = s[right]
            if c not in hash or hash[c] == 0:
                hash[c] = 1
                right += 1
                if right - left > max_length:
                    max_length = right - left
            else:
                # 从左开始找重复的字符
                while s[left] != s[right]:
                    # 删除滑动窗口划过的字典值
                    hash[s[left]] -= 1
                    left += 1
                # 找到left和right相同的字符
                hash[s[left]] -= 1
                left += 1
        return max_length



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s = "pwwkew"))

