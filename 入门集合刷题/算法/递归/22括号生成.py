'''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

    此题也可以用回溯的方法完成，见回溯部分
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.bracket_str_list = []
        def create_bracket(left_bracket : int, right_bracket:int, bracket_string : str):
            # 出口
            if left_bracket == 0 and right_bracket == 0:
                self.bracket_str_list.append(bracket_string)
                return
            # 条件
            if left_bracket > 0:
                create_bracket(left_bracket-1, right_bracket, bracket_string + '(')
            if right_bracket > left_bracket:
                create_bracket(left_bracket, right_bracket-1, bracket_string + ')')
        create_bracket(n, n, '')
        return self.bracket_str_list

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

