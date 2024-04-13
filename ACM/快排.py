
from typing import List


class quickSort:
    # def sort(self, nums: list, left: int, right: int):
    #     if left <= right:
    #         l = left; r = right
    #         pivot = nums[left]
    #         while l <= r:
    #             # 从左向右找比pivot大的
    #             while l <= r and nums[l] <= pivot:
    #                 l += 1
    #             while l <= r and nums[r] >= pivot:
    #                 r -= 1
    #             if l <= r:
    #                 nums[l], nums[r] = nums[r], nums[l]
    #                 r-=1; l+=1
            
    #         nums[r], nums[left] = nums[left], nums[r]
    #         self.sort(nums, left, r-1)
    #         self.sort(nums, r+1, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
            # heap_ = []
            # for num in nums:
            #     heap_.append(-num)
            # heapq.heapify(heap_)
            # for i in range(k-1):
            #     heapq.heappop(heap_)  # 弹出堆顶元素
            # return -heap_[0]
            return self.quickselect(nums, 0, len(nums)-1, k)

    # 快速选择算法
    def quickselect(self, nums: List[int], left, right, k):
        if left <= right:
            l = left; r = right
            pivot = nums[left]
            while l <= r:
                while l <= r and nums[l] <= pivot:
                    l += 1
                while l <= r and nums[r] >= pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1; r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            if r == len(nums) - k:
                return nums[r]
            elif r < len(nums) - k:
                return self.quickselect(nums, r+1, right, k)
            else:
                return self.quickselect(nums, left, r-1, k)

if __name__ == '__main__':
    q = quickSort()
    nums = [6, 5, 7, 10, 1, 100, -1]
    re = q.findKthLargest(nums, 3)
    print(re)
                
            