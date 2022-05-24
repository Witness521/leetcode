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
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.child[index]:
                node.child[index] = Trie()
            # 在最后一个字母的节点isEnd置为True
            if i == len(word)-1:
                node.isEnd = True
            node = node.child[index]


    def search(self, word: str) -> bool:
        node = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if i == len(word) - 1 and node.child[index] and node.isEnd == True:
                return True
            if node.child[index]:
                node = node.child[index]
            else:
                return False
        return False


    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            index = ord(char) - ord('a')
            if node.child[index]:
                node = node.child[index]
            else:
                return False
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('bcdea')
    print(obj.search('bcdea'))
    print(obj.startsWith('b'))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)