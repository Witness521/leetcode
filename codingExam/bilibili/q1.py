from typing import List

class Solution:
    def crackPassword(self, password: List[int]) -> str:
        
        def quickSort(nums: List, left, right):
            if left < right:
                pivot = left
                l, r = left, right
                while l <= r:
                    while l <= r and int(str(nums[l]) + str(nums[left])) <= int(str(nums[left]) + str(nums[l])):  # l在前 left在后小
                        l += 1
                    while l <= r and int(str(nums[r]) + str(nums[left])) >= int(str(nums[left]) + str(nums[r])):  # left在前 r在后小
                        r -= 1
                    if l <= r:
                        nums[l], nums[r] = nums[r], nums[l]
                nums[pivot], nums[r] = nums[r], nums[pivot]

                quickSort(nums, left, r-1)
                quickSort(nums, r+1, right)

        quickSort(password, 0, len(password)-1)
        return "".join(password)

Solution().crackPassword([15, 8, 7])