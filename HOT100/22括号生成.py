'''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
from typing import List

# 把二叉树先画出来，思路就出来了
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         answer = []
#         def backtrack(open, close, bracketStr: str):
#             if open == close == n:
#                 answer.append(bracketStr)
#                 return
#             if open < n:
#                 backtrack(open + 1, close, bracketStr + '(')
#             if close < open:
#                 backtrack(open, close + 1, bracketStr + ')')
#         backtrack(0, 0, '')
#         return answer

# if __name__ == '__main__':
#     print(Solution().generateParenthesis(1))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        # 回溯的方法
        def backtrace(left, right, S):
            if 2 * n == left + right:
                result.append(S)
                return
            if left < n:
                S += '('
                backtrace(left+1, right, S)
                S = S[:-1]
            if right < left:
                S += ')'
                backtrace(left, right+1, S)
                S = S[:-1]
        backtrace(0, 0, '')
        return result

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))