'''
给定一个列表 accounts，每个元素 accounts[i]是一个字符串列表，其中第一个元素 accounts[i][0]是名称 (name)，其余元素是 emails
表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，
它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。
'''
from typing import List

class Union:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, index):
        # 如果index根节点
        if self.parent[index] != index:
            # 寻找根节点并挂载在根节点上
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, i, j):
        # 将i的根节点挂载在j节点的根节点上
        self.parent[self.find(i)] = self.find(j)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = {}
        emailToName = {}

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in emailToIndex:
                    emailToIndex[account[i]] = len(emailToIndex)
                    emailToName[name] = name


