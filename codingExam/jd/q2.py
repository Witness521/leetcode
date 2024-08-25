
n, m = list(map(int, input().split()))
nHeight = list(map(int, list(input())))
mHeight = list(map(int, list(input())))

# shortCube = min(m, n)  # 从短的开始算
# longCube = max(m, n)
# if len(nHeight) > len(mHeight):
#     shortHeight = mHeight
#     longHeight = nHeight
# else:
#     shortHeight = nHeight
#     longHeight = mHeight

# min_length = n + m
# for start in range(shortCube):
#     valid = True
#     index = 0
#     for i in range(start, shortCube):
#         if shortHeight[i] + longHeight[index] > 3:
#             valid = False
#             index += 1
#             break
#     if valid:
#         if start + longCube > longCube:
#             min_length = start + shortCube
#         else:
#             min_length = longCube
#         break
# print(min_length)


def minLength(n, m, s, t):
    ans = n+m
    for i in range(len(s)):  # 将s从左边开始逐个消除
        if checkStr(s[i:], t):
            ans = min(ans, max(i + len(t), len(s)))
    
    for i in range(len(t)):
        if checkStr(s, t[i:]):
            ans = min(ans, max(i + len(s), len(t)))
    return ans


def checkStr(s, t):
    for i in range(min(len(s), len(t))):
        if s[i] == 2 and t[i] == 2:
            return False
    return True

if __name__ == '__main__':
    print(minLength(n, m, nHeight, mHeight))