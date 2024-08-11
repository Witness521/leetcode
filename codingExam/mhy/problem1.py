n = int(input())
nums = list(map(int, input().split()))

def getMaxAdjacentValue(nums):
    return max(nums[i] * nums[i+1] for i in range(len(nums)-1))

maxValue = getMaxAdjacentValue(nums)

for i in range(n-1):
    nums[i], nums[i+1] = nums[i + 1], nums[i]
    after_swap = [nums[i] * nums[i+1],
                   nums[i - 1] * nums[i] if i > 0 else float('-inf'),
                   nums[i + 1] * nums[i + 2] if i < n-2 else float('-inf')
                   ]
    nums[i], nums[i+1] = nums[i + 1], nums[i]
    maxValue = max(maxValue, max(after_swap))
    
print(maxValue)
