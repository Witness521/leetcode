'''给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if dict.get(word, None):
                dict[word] += 1
            else:
                dict[word] = 1
        sorted(dict.items(), key=lambda item:item[1])
        print(dict)
        for i in range(k):
            pass
        return [dict.popitem() for i in range(k)]

if __name__ == '__main__':
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))