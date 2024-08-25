s = list(input())
t = list(input())

def get_lcp(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
    return min(len(a), len(b))

def get_lcs(a, b):
    a = a[::-1]
    b = b[::-1]
    return get_lcp(a, b)

def findSimilarity(s, t):
    preLength, suffixLength = 0, 0
    minSim = 0
    # 从前往后找一个不一样的
    flag = True  # 全部一样
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            temp = s[i]
            s[i] = t[i]
            flag = False
            minSim = get_lcs(s, t) * get_lcp(s, t)
            s[i] = temp
            break
    if flag:
        return get_lcs(s, t) * get_lcp(s, t)
    
    rightIndex = -1
    while abs(rightIndex) <= min(len(s), len(t)):
        if s[rightIndex] != t[rightIndex]:
            temp = s[rightIndex]
            s[i] = t[rightIndex]
            minSim = max(minSim, get_lcs(s, t) * get_lcp(s, t))
            return minSim


print(findSimilarity(s, t))
