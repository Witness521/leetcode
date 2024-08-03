class Solution:
    def findk(self, nums: list, k: int, left: int, right: int):
      l = left; r = right
      pivot = nums[left]
      # 从左往右找比pivot大的
      while l <= r:
        while l <= r and pivot <= nums[l]:
          l += 1
        while l <= r and pivot >= nums[r]:
          r -= 1
        if l <= r:
          nums[l], nums[r] = nums[r], nums[l]
          l += 1
          r -= 1
      nums[left], nums[r] = nums[r], nums[left]
      if r == len(nums) - k:
        return nums[r]
      elif r < len(nums) - k:
        return self.findk(nums, k, r + 1, right)
      else:
        return self.findk(nums, k, left, r - 1)

s = Solution()
nums = [3,4,7,8,1,2]
result = s.findk(nums, 1, 0, len(nums)-1)
print(result)