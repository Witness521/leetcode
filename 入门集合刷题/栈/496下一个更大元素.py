from typing import List

'''
经典使用单调栈的题目
1. 使用单调栈的方法
2. 逆序往单调栈里面放置元素
3. 思路：站队，逆序看（从右往左看，看到的第一个高个）
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []  # 结果list
        stack = []  # 单调栈(由下至上是一个递减栈)
        map = {}

        nums2.reverse()  # num1翻转，逆序入栈
        for i in nums2:
            if len(stack) == 0:  # 如果栈为空
                map[i] = -1
                stack.append(i)
            else:
                while len(stack) != 0 and i > stack[len(stack) - 1]:  # 如果i大于栈顶元素
                    stack.pop()  # 栈顶元素出栈
                stack.append(i)  # i入栈
                # 如果i是栈底
                if len(stack) == 1:
                    map[i] = -1
                else:
                    map[i] = stack[len(stack)-2]

        for j in nums1:
            result.append(map[j])
        return result

if __name__ == '__main__':
    print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
        
