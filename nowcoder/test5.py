class Solution2:
    def decodeString(self, s: str) -> str:
        multi = 0
        res = ""  # 代表的是累计的字符
        result = ""
        stack = []
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif 'a' <= c <= 'z':
                res += c
            elif c == '[':
                stack.append((multi, res))
                multi = 0
                res = ""
            elif c == ']':
                cur_multi, last_res = stack.pop()
                result = result + last_res + cur_multi * res
                res = ""
        return result

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        result = [matrix[0][0]]
        visited[0][0] = 1
        def dfs(matrix, i, j, re, direct):
            rows, cols = len(matrix), len(matrix[0])
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for k in range(4):
                index = (k + direct) % 4
                x, y = directions[index][0], directions[index][1]
                if rows > i + x >= 0 and cols > j + y >= 0 and visited[i+x][y+j] == 0:
                    re.append(matrix[i+x][j+y])
                    visited[i+x][j+y] = 1
                    dfs(matrix, i + x, j + y, re, index)
                    break
        
        dfs(matrix, 0, 0, result, 0)
        return result


if __name__ == '__main__':
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))