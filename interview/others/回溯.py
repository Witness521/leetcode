from typing import List

result = []

class Solution:    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [], 0)
        return result

    # 枚举回溯
    def dfs(self, nums: List[int], re: List[int], i: int):
        
        result.append(re.copy())
        for j in range(i, len(nums)):
            re.append(nums[j])
            self.dfs(nums, re, j+1)
            re.pop()


if __name__ == '__main__':
    Solution().subsets([1,2,3])
    print(result)