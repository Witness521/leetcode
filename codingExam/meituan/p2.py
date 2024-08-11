

def min_cost(a, x, k):
    n = len(a)
    dp = [0] * (n + 1)
    hashSet = set()
    mex = 0

    for i in range(n - 1, -1, -1):
        # 代表从i开始清空的最小代价
        dp[i] = dp[i + 1] + x

        hashSet.add(a[i])
        while mex in hashSet:
            mex += 1

        dp[i] = min(dp[i], k * mex)

    return dp[0]

def cal_min_left_to_right(a, x, k):
    hashmap = {}
    maxKey = 0
    for i in a:
        maxKey = max(i, maxKey)
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    # 更新mex的值
    mex = maxKey
    for i in range(1, maxKey):
        if i not in hashmap:
            mex = i
    
    minCost = 2e5
    for index, i in enumerate(a):
        if hashmap[i] == 1 and mex > i:
            mex = i
            hashmap.pop(i)
        minCost = min(minCost, x * (index + 1) + mex * k)
    return minCost

        




T = int(input())
for _ in range(T):
    n,k,x = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    print(cal_min_left_to_right(ai, x, k))