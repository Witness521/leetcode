'''
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
'''

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
            if char not in node:
                return False
            node = node[char]
        return '#' in node


    def startsWith(self, prefix: str) -> bool:
        node = self.child
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True

if __name__ == '__main__':
    obj = Trie()
    obj.insert('bcdea')
    print(obj.search('bcdea'))
    print(obj.startsWith('b'))