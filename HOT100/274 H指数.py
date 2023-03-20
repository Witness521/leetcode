'''
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h指数。

根据维基百科上h 指数的定义：h 代表“高引用次数”，一名科研人员的 h指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
且其余的 n - h篇论文每篇被引用次数不超过 h 次。

如果 h 有多种可能的值，h 指数 是其中最大的那个。
'''
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # 将citations进行反向排序
        h = 0
        for i in range(1, len(citations) + 1):
            if citations[i-1] >= i:  # 如果citations
                h += 1
        return h  # [100]的情况

if __name__ == '__main__':
    print(Solution().hIndex([3,0,6,1,5]))

