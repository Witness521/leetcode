'''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

    此题也可以用递归的方法完成，见递归部分
'''
from typing import List


# 回溯是从上往下，递归是从下往上
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.bracket_str_list = []

        def create_bracket(left_bracket: int, right_bracket: int, bracket_string: List[str]):
            # 出口
            if left_bracket == n and right_bracket == n:
                self.bracket_str_list.append(''.join(bracket_string))
                return
            # 条件
            if left_bracket < n:
                bracket_string.append('(')
                create_bracket(left_bracket + 1, right_bracket, bracket_string)
                bracket_string.pop()
            if left_bracket > right_bracket:
                bracket_string.append(')')
                create_bracket(left_bracket, right_bracket + 1, bracket_string)
                bracket_string.pop()

        create_bracket(0, 0, [])
        return self.bracket_str_list


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
