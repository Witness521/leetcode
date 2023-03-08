'''
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
from typing import List

# 使用树的数据结构  算法采用 dfs 或 BFS

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if digits == "":
        #     return []
        # phone_dict = {
        #     '2': 'abc',
        #     '3': 'def',
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "pqrs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }
        #
        # total_result = []
        # def dfs(i, result: str):
        #     if i >= len(digits):
        #         total_result.append(result)
        #         return
        #     for ch in phone_dict[digits[i]]:
        #         dfs(i+1, result + ch)
        # dfs(0, '')
        # return total_result
        if digits == "":
            return None
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result_list = []
        def dfs(digits: str, result: str, i: int):
            if i == len(digits):
                result_list.append(result)
                return
            for c in hashmap[digits[i]]:
                dfs(digits, result + c, i + 1)
        dfs(digits, '', 0)
        return result_list




if __name__ == '__main__':
    print(Solution().letterCombinations("23"))

