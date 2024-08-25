
# n, k = list(map(int, input().split()))
# nums = list(map(int, input().split()))

# def solution(nums, k):
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
    
#     dp = [0] * n
#     dp[0] = nums[0]
    
#     for i in range(1, n):
#         if i < k:
#             dp[i] = max(dp[i-1], nums[i])
#         else:
#             dp[i] = max(dp[i-1], dp[i-k] + nums[i])
    
#     return dp[-1]

# print(solution(nums, k))


n, k = list(map(int, input().split()))
nlist = list(map(int, input().split()))

def solution():
    if len(nlist) <= k:
        return max(nlist)
    dp = [0] * len(nlist)
    for i in range(k):
        dp[i] = max(nlist[:i+1])
    
    for i in range(k, len(nlist)):
        for j in range(k):
            dp[i] = max(dp[i-k] + nlist[i], dp[i-j], dp[i])
    return dp[-1]
print(solution())