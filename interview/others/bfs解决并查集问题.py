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

n = int(input())
data = []
for i in range(n):
    line = input().split()
    data.append(list(map(int, line)))

collection = {}
for i in range(n):
    for j in range(i, n):
        if data[i][j] > 0:
            # 保留元素之间的关系
            if i not in collection:
                collection[i] = (j,)
            else:
                collection[i].add(j)

            if j not in collection:
                collection[j] = (i,)
            else:
                collection[j].add(i)

visited = [False] * n
def bfs(start):
    queue = [start]
    visited[start] = True
    group = []
    while queue:
        node = queue.pop(0)
        group.append(node)
        if node in collection:
            for neighbor in collection[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    return group

sums = []
for i in range(n):
    if not visited[i]:
        group = bfs(i)
        sum_sim = 0
        for a in range(len(group)):
            for b in range(a + 1, len(group)):
                sum_sim += data[group[a]][group[b]]
        sums.append(sum_sim)

sums.sort(reverse=True)
print(' '.join(map(str, sums)))
        
            

