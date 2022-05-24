'''
给出一个字符串数组words 组成的一本英语词典。返回words 中最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
'''
from typing import List

class Trie:
    def __init__(self):
        self.child = {}

    def insert(self, word: str) -> None:
        node = self.child
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = {}

    def search(self, word: str) -> bool:
        node = self.child
        for char in word:
            # 如果字符存在于字符串 and 字符对应的字典value里面有#
            if char in node and '#' in node[char]:
                node = node[char]
            else:
                return False
        return '#' in node


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longest = ''
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest


if __name__ == '__main__':
    print(Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))