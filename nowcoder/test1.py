import queue
from collections import deque


def judge(n, m, startX, startY, x, y):
    if n > startX + x >= 0 and m > startY + y >= 0:
        return True
    return False


def bfs(n, m, x1, y1, x2, y2):
    queue1 = deque(); queue1.append([x1, y1])
    queue2 = deque(); queue2.append([x2, y2])
    visited = set()
    visited.add((x1-1, y1-1))
    visited.add((x2-1, y2-1))
    count = 2
    while queue1 and queue2:
        x1, y1 = queue1.popleft()
        x2, y2 = queue2.popleft()
        x1, x2, y1, y2 = x1-1, x2-1, y1-1, y2-1
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if judge(n, m, x1, y1, x, y) and judge(n, m, x2, y2, x, y):
                if (x1+x, y1+y) not in visited or (x2+x, y2+y) not in visited:
                    visited.add((x1+x, y1+y))
                    visited.add((x2+x, y2+y))
                    queue1.append((x1+x, y1+y))
                    queue2.append((x2+x, y2+y))
    print(visited)
    return n * m - len(visited)
    
            
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    n, m = nums[0], nums[1]
    startX1, startY1 = nums[2], nums[3]
    startX2, startY2 = nums[4], nums[5]
    count = bfs(n, m, startX1, startY1, startX2, startY2)
    print(count)