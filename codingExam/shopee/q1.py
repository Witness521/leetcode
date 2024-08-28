
class Solution:
    def bestFit(self, V, item) :
        n = len(item)
        dp = [[0] * (V+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, V+1):
                dp[i][j] = dp[i-1][j]
                if item[i-1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-item[i-1]] + item[i-1])
        
        closeNum = dp[n][V]
        return V - closeNum
    
if __name__ == '__main__':
    print(Solution().bestFit(24, [8,3,12,7,9,7]))