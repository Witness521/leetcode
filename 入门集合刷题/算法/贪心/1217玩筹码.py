'''
有n个筹码。第 i 个芯片的位置是position[i]。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个芯片的位置从position[i]改变为:

position[i] + 2或position[i] - 2，此时cost = 0
position[i] + 1或position[i] - 1，此时cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。
'''
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # because move 2 step cost 0, so that compares the number of odd position and even position
        odd_num = 0
        even_num = 0
        for i in position:
            if i % 2:
                odd_num += 1  # 奇数
            else:
                even_num += 1  # 偶数
        return min(odd_num, even_num)

if __name__ == '__main__':
    print(Solution().minCostToMoveChips([1,2,2,2,2]))
