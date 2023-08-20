"""
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，
再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
如果无解，请返回-1
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
from typing import List


class Solution:
    def minMoney(self , arr: List[int], aim: int) -> int:
        dp = [float('inf')] * (aim+1)
        if len(arr) < 1:
            return -1
        if aim < min(arr) and aim != 0:
            return -1
        elif aim == 0:
            return 0
        # 先初始化一下
        dp[0] = 0
        for i in range(0, aim+1):
            for j in arr:
                if i - j < 0:
                    continue
                dp[i] = min(dp[i], dp[i-j] + 1)
        if dp[aim] == float("inf"):
            return -1
        else:
            return int(dp[aim])
    

if __name__ == '__main__':
    print(Solution().minMoney([5,2,3], 20))