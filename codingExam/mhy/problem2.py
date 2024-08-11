
n, m, k = list(map(int, input().split()))
wList = []
valList = []
for _ in range(n):
    w, val = list(map(int, input().split()))
    wList.append(w)
    valList.append(val)

def insertIntoMap(k, v, exclusions):
    if k in exclusions:
        exclusions[k].add(v)
    else:
        temp = set()
        temp.add(v)
        exclusions[k] = temp

exclusions = {}
for _ in range(k):
    a, b = list(map(int, input().split()))
    insertIntoMap(a, b, exclusions)
    insertIntoMap(b, a, exclusions)

def checkValid(contains, excluList):
    for contain in contains:
        if contain in excluList:
            return False
    return True

maxVal = 0
def dfs(contains, wtotal, valTotal, startIndex):
    global maxVal
    if wtotal > m:
        return
    elif valTotal > maxVal:
        maxVal = valTotal
    
    i = startIndex
    for i in range(startIndex, n+1):
        excluList = exclusions[i]
        if not checkValid(contains, excluList) or wtotal + wList[i-1] > m:
            continue
        
        contains.append(i)
        dfs(contains, wtotal + wList[i-1], valTotal + valList[i-1], i+1)
        contains.pop()

dfs([], 0, 0, 1)
print(maxVal)
    

