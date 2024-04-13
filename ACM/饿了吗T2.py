'''
小红定义两个数组是互补的，当且仅当数组每一个位置的数字之和都相同。

小红有两个长度为的数组，分别是a和b，她想知道有多少个子序列对应的数组是互补的。
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def cal_min_cost(n: int, a: list, b: list):
    # 因为任意一个位置，a[i]+b[i]都为4，因此有3个4，我们可以考虑选或者不选（至少要选1个位置）
    # 总的情况就是2^3 - 1 = 7
    counts = {}
    mod = 1e9 + 7
    for i in range(len(a)):
        counts[a[i] + b[i]] = counts.get((a[i] + b[i]), 0) + 1
    twos = [1] * (n+1)
    for i in range(1, n+1):
        twos[i] = twos[i-1] * 2
    
    sum = 0
    for key, value in counts.items():
        sum = (sum + (twos[value] - 1) % mod) % mod
    print(sum)


cal_min_cost(n, a, b)