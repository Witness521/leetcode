'''
编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
'''

from typing import List


class Solution:
    # 属于将题目想简单了
    # def searchMatrix_(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] < target:
        # index = 0
        # # 定位列开始查找
        # for j in range(len(matrix[0])):
        #     if matrix[0][j] > target:  # 如果第一列的元素大于target
        #         index = j - 1
        #         break
        #     elif matrix[0][j] == target:
        #         return True
        #     else:  # matrix[0][j] < target
        #         index = j
        # # 从刚才找到的那一列往下找
        # for i in range(len(matrix)):
        #     if matrix[i][index] == target:
        #         return True
        #
        # # 定位行开始查找
        # index = 0
        # for i in range(len(matrix)):
        #     if matrix[i][0] > target:  # 如果第一列的元素大于target
        #         index = i - 1
        #         break
        #     elif matrix[i][0] == target:
        #         return True
        #     else:
        #         index = i
        # # 从刚才找到的那一行往下找
        # for j in range(len(matrix[0])):
        #     if matrix[index][j] == target:
        #         return True
        #
        # return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角开始，当作二叉搜索树
        i = 0
        j = len(matrix[0]) - 1
        row = len(matrix)  # line number
        while i < row and j >= 0:
            if matrix[i][j] < target:
                i = i + 1
            elif matrix[i][j] > target:
                j = j - 1
            else:
                return True
        return False





if __name__ == '__main__':
    print(Solution().searchMatrix([[1,3,5,7,9],
                                   [2,4,6,8,10],
                                   [11,13,15,17,19],
                                   [12,14,16,18,20],
                                   [21,22,23,24,25]]
,13))