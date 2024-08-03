import math
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        self.visited = [False] * len(nums)
        self.nums = nums
        self.count = 0
        self.dfs([])
        return self.count
        
    def dfs(self, temp: list):
        if len(temp) == len(self.nums):
            self.count += 1
            print(temp)
            return
        
        for i, num in enumerate(self.nums):
            if self.visited[i] or (i > 0 and not self.visited[i-1] and self.nums[i] == self.nums[i-1]):
                continue
            
            if len(temp) == 0 or (len(temp) >= 1 and self.judge(temp[-1] + self.nums[i])):
                self.visited[i] = True
                temp.append(num)
                self.dfs(temp)
                self.visited[i] = False
                temp.pop()
    
    def judge(self, num):
        if num < 0:
            return False
        kaifang = int(math.sqrt(num))
        if kaifang * kaifang == num:
            return True
        return False


if __name__ == '__main__':
    a = Solution().numSquarefulPerms([1,17,8])
    print(a)


