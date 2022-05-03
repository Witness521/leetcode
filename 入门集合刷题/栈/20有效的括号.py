'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。'''
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        # 如果为奇数个则返回false
        if len(s) % 2 == 1:
            return False
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                # 左括号没有右括号来匹配
                if len(stack) == 0: return False
                left_parenthesis = stack.pop()
                if c == ')':
                    if left_parenthesis == '(': continue
                    return False  # 没有匹配成功
                elif c == ']':
                    if left_parenthesis == '[': continue
                    return False  # 没有匹配成功
                elif c == '}':
                    if left_parenthesis == '{': continue
                    return False  # 没有匹配成功
                else:
                    return False
        # 当字符串遍历完之后，若栈不为空则说明还有左括号没被匹配
        return len(stack) == 0

if __name__ == '__main__':
    print(Solution().isValid('(('))
