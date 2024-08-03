'''
这里有几个正整数，
𝑎1...𝑎𝑛，塔子哥 会先去掉其中最多𝑑个数
小明 接下来会将剩余的数中最多𝑚个数乘以−𝑘

塔子哥 想要剩余数之和尽可能大，小明 想要剩余数之和尽可能小。

假设 塔子哥 和 小明 都足够聪明，请问最后剩余数之和是多少。
'''

# T = int(input())
# for _ in range(T):
#     n, m, k, d = list(map(int, input().split()))
#     a_n = list(map(int, input().split()))

#     max_remain = 0
#     a_n = sorted(a_n, reverse=True)
#     for i in range(d+1):
#         a_n_i = a_n[i:]
#         remain = -k * sum(a_n_i[:m]) + sum(a_n_i[m:])
#         if remain > max_remain:
#             max_remain = remain

# print(max_remain)

T = int(input())
for _ in range(T):
    n, m, k, d = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums = sorted(nums, reverse=True)
    tmp = -k * sum(nums[:m]) + sum(nums[m:])
    res = tmp
    for i, num in enumerate(nums):
        if i >= d:
            break
        # 将滑动窗口左面的元素出队
        tmp += k * nums[i]
        # 滑动窗口右面的元素如果在数组范围内则入队
        if i + m < n:
            tmp -= (k+1) * nums[i+m]
        res = max(res, tmp)
    print(res)