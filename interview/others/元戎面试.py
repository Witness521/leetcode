# python

# n = int(input())
# nums = list(map(int, input().split()))

n = 5
nums = [21, 21, -40, -1, 21, -2]

# dp代表包含第i个数的最大连续字段和
dp = [0] * len(nums)
dp[0] = nums[0]
for i in range(len(nums)-1, -1, -1):
    pre = (i + 1) % len(nums)
    dp[i] = max(dp[pre] + nums[i], nums[i])
for i in range(0, len(nums)):
    pre = (i-1) % len(nums)
    dp[i] = max(dp[pre] + nums[i], nums[i])

print(max(dp))

# 21 21 -40 -1 21 -2

# 21 + -2  -2
# dp[5] 19
# dp[4] 40
# dp[3] 39
# dp[2] -1
# dp[1] 21
# dp[0] 42
