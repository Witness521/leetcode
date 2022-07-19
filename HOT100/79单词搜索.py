'''
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 从首个字母开始进行dfs
        def dfs(board, word, isvisited, i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            # 将节点设置成访问状态
            isvisited[i][j] = 1

            for dir in directions:
                newi = i + dir[0]
                newj = j + dir[1]
                if 0 <= newi < row and 0 <= newj < col:
                    if isvisited[newi][newj] == 0:
                        if dfs(board, word, isvisited, newi, newj, k+1):
                            return True
            # 重点！！！犯过错
            # 记得将节点状态改回未访问，因为此处已经回溯
            isvisited[i][j] = 0

        for i in range(row):
            for j in range(col):
                isvisited = [[0] * col for _ in range(row)]
                if board[i][j] == word[0]:
                    if dfs(board, word, isvisited, i, j, 0):
                        return True
        return False

if __name__ == '__main__':
    print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

# [
#     ["A","B","C","E"],
#     ["S","F","E","S"],
#     ["A","D","E","E"]
# ]