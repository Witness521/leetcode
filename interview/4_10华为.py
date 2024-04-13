
n = int(input())
lst = []
ss = set()
for i in range(n):
    s = tuple(input().split(','))
    t = s[0] + s[1] + s[2]
    if t not in ss:
        lst.append(s)
        ss.add(t)

fac = dict()

m = int(input())
for i in range(m):
    s = input().split(',')
    fac[s[0]] = int(s[1])

val = dict()
for i in lst:
    if i[1] not in val:
        val[i[1]] = 0

    val[i[1]] += fac[i[2]] * int(i[3])

ans = []
for i, j in val.items():
    ans.append((i, j))

ans.sort(key=lambda x: x[0])

for i in ans:
    print(f'{i[0]},{i[1]}')