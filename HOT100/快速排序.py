from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def Paritition(kvList, left, right):
            temp = kvList[left]
            while left < right:
                # 从右往左找比temp小的
                while left < right and kvList[right][1] >= temp[1]:
                    right -= 1
                kvList[left] = kvList[right]
                while left < right and kvList[left][1] <= temp[1]:
                    left += 1
                kvList[right] = kvList[left]
                # 把temp数据放入最终空出的坑中
                kvList[left] = temp
                return left

        def quickSort(kvList, left, right):
            if left < right:
                index = Paritition(kvList, left, right)
                if index > k:
                    quickSort(kvList, left, index - 1)
                elif index < k:
                    quickSort(kvList, index + 1, right)
                else:
                    return


        # 用快速排序试试
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        kvList = []
        for key, value in map.items():
            kvList.append((key, value))

        if len(kvList) == 1:
            return [kvList[0][0]]

        quickSort(kvList, 0, len(kvList)-1)
        kvList.reverse()
        return [_[0] for _ in kvList[:k]]

        #         quickSort(nums, 0, left)
        #         quickSort(nums, left+1, len(nums)-1)
        # quickSort(nums, 0, len(nums)-1)
        # print(nums)

if __name__ == '__main__':
    print(Solution().topKFrequent(nums = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3], k = 3))