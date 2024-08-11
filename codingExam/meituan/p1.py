
n = int(input())
password = input()

hashmap = {}
containMap = {}
for _ in range(n):
    s = input()
    if s in containMap:  # 如果已经尝试过
        continue

    length = len(s)
    containMap[s] = 1
    if length not in hashmap:
        hashmap[length] = 1
    else:
        hashmap[length] += 1
    
lenPass = len(password)
count = 0
for l in range(1, lenPass):
    if l in hashmap:
        count += hashmap[l]
    
maxCount = count + hashmap[lenPass]
minCount = count + 1
print(minCount, end=" ")
print(maxCount)