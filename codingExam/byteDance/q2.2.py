# 给定一个数和一个数组, 求这个数组能组成的不超过这个数的最大值

# 22310   [2, 4, 9]

nums = "20000"
A = [2, 4, 9]

def findNoMoreNum(nums, AList):
    if not isValid(nums, AList):
        return "".join([str(max(A))] * (len(nums) - 1))
    
    reverseA = AList[::-1]
    result = []
    for index, num in enumerate(nums):
        for a in reverseA:
            if a == int(num):
                result.append(a)
            elif a < int(num):
                result.append(a)
                # 此时后面均可以加最大值
                while index < len(nums)-1:
                    result.append(max(A))
                    index += 1
                return "".join(map(str, result))



def isValid(nums, AList):
    minA = min(AList)
    for num in nums:
        if minA < int(num):
            return True
        elif minA == int(num):
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    print(findNoMoreNum(nums, A))