# 归并排序
def mergeSort(nums: list, l: int, r: int):
    if l >= r:
        return
    # 从中间进行分治
    mid = (l + r) // 2
    mergeSort(nums, l, mid)
    mergeSort(nums, mid + 1, r)

    # 合并
    temp = []
    i = l; j = mid + 1
    while i <= mid and j <= r:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    temp += nums[i : mid+1]
    temp += nums[j : r+1]
    nums[l:r+1] = temp[:]

if __name__ == '__main__':
    nums = [8, 4, 5, 7]
    mergeSort(nums, 0, len(nums) - 1)
    print(nums)