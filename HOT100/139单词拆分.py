'''
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
'''
from typing import List


class Solution:
    ############################## DFS的方法 ###################
    # def __init__(self):
    #     self.result = False
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     def dfs(right: int):
    #         if right == len(s):
    #             self.result = True
    #         for word in wordDict:
    #             if word == s[right:right + len(word)]:
    #                 dfs(right + len(word))
    #     dfs(0)
    #     return self.result

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     import functools
    #     @functools.lru_cache(None)  # 装饰器 用于存储递归过程中经常使用的实例的结果
    #     def dfs(right: int):
    #         if right == len(s):
    #             return True
    #         for word in wordDict:
    #             if word == s[right:right + len(word)]:
    #                 return dfs(right + len(word))
    #         return False  # 只要在递归的后面加上返回就不会出现return None的情况
    #     return dfs(0)

    ############################ DP的方法 ###########################
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[len(s)]


if __name__ == '__main__':
    print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
