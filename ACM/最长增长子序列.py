

def longestIncrSeq(array: list[int]):
    dp = [1] * len(array)  # dp为包含第i个元素的最长递增子序列的长度
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        num = int(input())
        array.append(num)
    
    print(longestIncrSeq(array))
