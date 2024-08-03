def dfs(n, edges):
    graph = [[] for _ in range(n)]
    for x, y, w in edges:
        graph[x-1].append((w, y-1))
        graph[y-1].append((w, x-1))

    distances = [float('inf')] * n
    distances[0] = 0
    pri_que = [(0, 0)]
    while pri_que:
        cur_dis, cur_node = heapq.heappop(pri_que)

        if cur_dis > distances[cur_node]:
            continue
        
        for weight, neightbor in graph[cur_node]:
            distance = cur_dis + weight

            if distance < distances[neightbor]:
                distances[neightbor] = distance
                heapq.heappush(pri_que, (distance, neightbor))
    print(distances)
    return sum(distances)

n = int(input())
edges = []
for _ in range(n-1):
    x, y, w = map(int, input().split())
    edges.append((x, y, w))

result = dfs(n, edges)
print(result)