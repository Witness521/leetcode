# 归并排序
from typing import List

def merge_sort(nums: List[int], l: int, r: int):
    if l >= r:  # 一个元素时就返回 分
        return
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)

    # 合并
    temp = []
    i = l; j = mid + 1
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    temp += nums[i : mid + 1]
    temp += nums[j : r + 1]

    nums[l: r+1] = temp
    


if __name__ == '__main__':
    nums = [-1, 0,1,2,-1,-4]
    merge_sort(nums, l=0, r=5)
    print(nums)