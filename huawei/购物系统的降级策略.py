

def getCnt():
    list1 = list(map(int, input().split()))
    target = int(input())

    # 二分法计算
    if sum(list1) == target:
        print(-1)
        return
    
    l = 0; r = max(list1)
    while l <= r:
        mid = (l + r) // 2
        sum_ = 0
        for num in list1:
            sum_ += min(num, mid)
        if sum_ > target:
            r = mid - 1
        else:
            l = mid + 1
    print(r)
        



getCnt()