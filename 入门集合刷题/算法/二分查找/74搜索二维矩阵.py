'''
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # 二分法
        left = 0
        right = len(matrix) - 1  # 代表matrix的一维长度
        row = 0
        while left <= right:
            mid = (left+right) // 2
            if matrix[mid][0] < target:
                left = mid + 1  #### 这块不是mid+1，因为mid是一行数据，不是一个数据, 所以用row保存
                row = mid
            elif matrix[mid][0] > target:
                right = mid - 1
                row = mid - 1
            else:  # 直接找到了
                return True
        for i in matrix[row]:
            if target == i:
                return True
        return False

    '''
        另一种方法，将二维数组看作一维的数组
    '''
    def searchMatrixIn1(self, matrix: List[List[int]], target: int):
        left = 0
        row = len(matrix)
        column = len(matrix[0])
        right = row * column - 1
        while left <= right:
            mid = left + (right - left) // 2
            row_temp = mid // column
            col_temp = mid % column
            if matrix[row_temp][col_temp] == target:
                return True
            elif matrix[row_temp][col_temp] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False



if __name__ == '__main__':
    print(Solution().searchMatrixIn1([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
