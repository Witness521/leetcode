'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 方法一 暴力解法
        length1 = len(nums1)
        length2 = len(nums2)
        merge_list = []
        index1 = 0
        index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                merge_list.append(nums1[index1])
                index1 += 1
            else:
                merge_list.append(nums2[index2])
                index2 += 1
        # 将未合并的元素放入list
        while index1 < length1:
            merge_list.append(nums1[index1])
            index1 += 1
        while index2 < length2:
            merge_list.append(nums2[index2])
            index2 += 1

        median = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:  # 偶数
            return (merge_list[median] + merge_list[median-1]) / 2
        else:
            return merge_list[median]

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3], [2]))