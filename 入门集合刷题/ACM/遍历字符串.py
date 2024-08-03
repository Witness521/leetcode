

# def convert(s):
#     list = []
#     for c in s:
#         c = c.upper()
#         list.append(c)
#     str = ''.join(list)
#     print(str)

# convert('abc')

# 回溯算法
# 求组合数为2的所有结果  result不能写为参数的原因是函数递归执行 后面的值会覆盖前面的
class Solution:
    def __init__(self) -> None:
        self.result = []

    def backTracing(self, nums: list, k: int, startIndex: int, path: list):
        # 写递归的出口
        if len(path) == k:
            # self.result.append(path.copy())
            return
        
        for i in range(startIndex, len(nums)):
            self.result.append(path.copy())
            path.append(nums[i])
            # 递归需要从i+1的位置, 因为从i开始又会重复计算i的值
            self.backTracing(nums, k, i+1, path)
            # 还需要将加入的元素删除, 这样才会实现1 3 而不是 1 2 3
            path.pop()

# s = Solution()
# s.backTracing([1, 2, 3, 4], 2, 0, [])
# print(s.result)
            
print('A'.isalpha())