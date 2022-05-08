'''给定数组people。people[i]表示第 i个人的体重，船的数量不限，每艘船可以承载的最大重量为limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。

返回 承载所有人所需的最小船数。'''
'''
    重点是双人船，所以可以使用贪心算法求解 最重匹配最轻
'''
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatNum = 0
        people.sort(reverse=True)  # 降序排列
        left = 0
        right = len(people) - 1
        while left < right:
            if people[left] + people[right] <= limit:
                boatNum += 1
                left += 1
                right -= 1
            else:
                boatNum += 1
                left += 1
        return boatNum