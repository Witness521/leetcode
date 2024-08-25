# 快速排序

# 递归的思想 O(nlogn)
def quickSort(nums: list[int], left: int, right: int):
    if left < right:
        pivot = left
        l = left; r = right
        while l <= r:
            # 从左向右找比pivot大的
            while l <= r and nums[l] <= nums[pivot]:
                l+=1
            # 从右向左找比pivot小的
            while l <= r and nums[r] >= nums[pivot]:
                r-=1
            # 交换left right
            if l <= r:  # 不要忘记, 否则最后一轮会出现错误
                nums[l], nums[r] = nums[r], nums[l]
        
        # r在左
        nums[r], nums[pivot] = nums[pivot], nums[r]
        quickSort(nums, left, r-1)
        quickSort(nums, r+1, right)

if __name__ == '__main__':
    nums = [2, 1, 5, 2, 0, 9, 1]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)

    a = 'a'
    print(ord(a))