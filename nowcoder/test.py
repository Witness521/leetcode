

def findMinPossibleNumber (allSum, A):
    if allSum < 0:
        return 0
    if A <= 0:
        return 0
    if allSum == A:
        return 1

    max_count = allSum // A
    for count in range(1, max_count + 1):
        if (allSum - count * A) % 10 == 0:
            return count

    return -1

def longIncreasingSeq(nums: list):
    dp = [1] * len(nums)  # 代表包含第i个元素的最长子序列
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

def maxScore(cardPoints, k: int) -> int:
        # 滑动窗口求最小的连续
        winSize = len(cardPoints) - k
        sumContinue = sum(cardPoints[:winSize])
        minContinue = sumContinue
        for index in range(winSize, len(cardPoints)):
            sumContinue = sumContinue - cardPoints[index-winSize] + cardPoints[index]
            print(sumContinue)
            if minContinue > sumContinue:
                minContinue = sumContinue
        
        print(minContinue)
        return sum(cardPoints) - minContinue



if __name__ == '__main__':
    # print(findMinPossibleNumber(10258, 9))
    # print(longIncreasingSeq([10,9,2,5,3,7,101,18]))
    maxScore([1,79,80,1,1,1,200,1], 3)