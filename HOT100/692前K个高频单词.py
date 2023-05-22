import heapq
from typing import List

class Word:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        if self.value != other.value:
            return self.value < other.value
        return self.key > other.key  # 从小到大

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = {}
        for word in words:
            if word not in map:
                map[word] = 1
            else:
                map[word] += 1
        hp = []
        for key, value in map.items():
            heapq.heappush(hp, Word(key, value))
            while len(hp) > k:
                heapq.heappop(hp)
        result = []
        while hp:
            result.append(heapq.heappop(hp).key)
        # hp.sort(reverse= True)
        return result[::-1]


if __name__ == '__main__':
    print(Solution().topKFrequent(
["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))