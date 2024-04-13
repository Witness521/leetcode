
# class S:
#     def __init__(self):
#         self.count = 0

#     def func(self):
#         n = int(input())
#         nums = []
#         result = []
#         for _ in range(n):
#             num = list(map(int, input().split()))
#             nums.append(num)
#         # 只需要看这个矩阵的一半就可以
#         for i in range(n):
#             for j in range(i, n):
#                 self.count = 0
#                 if nums[i][j]:
#                     self.count += nums[i][j]
#                     nums[i][j] = 0
#                     self.find(nums, n, j)
#                     result.append(self.count)
#                     self.count = 0
#         result = sorted(result, reverse=True)
#         for i in result:
#             if i != 0:
#                 print(i, end=' ')
#         # print(result)
#                     #for k in range(j, n):
#                     #    if nums[j][k]:
#                     #        count += nums[j][k]
#                     #        nums[j][k] = 0
                            
#     def find(self, nums, n, j):
#         for k in range(j, n):
#             if nums[j][k]:
#                 self.count += nums[j][k]
#                 nums[j][k] = 0
#                 self.find(nums, n, k)

# for i in range(len(result)):
#     print(str(result[i]), end="")
#     if i != len(result)-1:
#         print(' ', end="")

# if __name__ == "__main__":
#     s = S()
#     s.func()

"""
小明想要处理一批图片，将相似的图片分类。他首先对图片的特征采样，得到图片之间的相似度，然后按照以下规则判断图片是否可以归为一类: 
1)相似度>0表示两张图片相似; 
2)如果A和B相似，B和C相似，但A和C不相似。那么认为A和C间接相似，可以把ABC归为一类，但不计算AC的相似度: 
3)如果A和所有其他图片都不相似，则A自己归为一类，相似度为0。给定一个大小为的矩阵存储任意两张图片的相似度，M]即为第个图片和第个图片的相似度，请按照"从大到小"的顺序返回每个相似类中所有图片的相似度之和。
5
0 0 50 0 0
0 0 0 25 0
50 0 0 0 15
0 25 0 0 0
0 0 15 0 0
"""


def find(x, f):
    if f[x] == x:
        return x
    f[x] = find(f[x], f)
    return f[x]

def merge(x, y, g, f, v):
    fx = find(x, f)
    fy = find(y, f)
    if fx != fy:
        f[fx] = fy
        v[fy] += v[fx] + g
    else:
        v[fy] += g

n = int(input())
a = []
f = [i for i in range(n)]
v = [0] * n

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(n):
        if row[j] > 0:
            merge(i, j, row[j], f, v)

print(v)
res = []
for i in range(n):
    if f[i] == i:
        res.append(v[i] // 2)

res.sort(reverse=True)

# 对list、set等进行解包 按照空格分隔打印出每个元素
print(*res)