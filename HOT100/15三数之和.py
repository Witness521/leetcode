'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''
# 第一次没想出来  第二次还没想出来(试一下回溯,相当于全部遍历)

from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#         # 遍历每一个数，然后将三数之和问题变成两数之和的问题
#         for i in range(len(nums) - 2):
#             if i == 0 or nums[i] != nums[i-1]:
#                 left = i + 1
#                 right = len(nums) - 1
#                 left_num = 0 - nums[i]
#                 while left < right:
#                     if nums[left] + nums[right] < left_num:
#                         left += 1
#                     elif nums[left] + nums[right] > left_num:
#                         right -= 1
#                     else:
#                         result.append([nums[i], nums[left], nums[right]])
#                         # 去重
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
#                         left += 1
#                         right -= 1
#         return result

# # class Solution:
# #     def threeSum(self, nums: List[int]) -> List[List[int]]:
# #         n = len(nums)
# #         nums.sort()
# #         result = list()
        
# #         # 枚举 a
# #         for i in range(n):
# #             # 需要和上一次枚举的数不相同
# #             if i > 0 and nums[i] == nums[i - 1]:
# #                 continue
# #             # c 对应的指针初始指向数组的最右端
# #             k = n - 1
# #             target = -nums[i]
# #             # 枚举 b
# #             for j in range(i + 1, n):
# #                 # 需要和上一次枚举的数不相同
# #                 if j > i + 1 and nums[j] == nums[j - 1]:
# #                     continue
# #                 # 需要保证 b 的指针在 c 的指针的左侧
# #                 while j < k and nums[j] + nums[k] > target:
# #                     k -= 1
# #                 # 如果指针重合，随着 b 后续的增加
# #                 # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
# #                 if j == k:
# #                     break

# #                 if nums[j] + nums[k] == target:
# #                     result.append([nums[i], nums[j], nums[k]])
        
# #         return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 使用双指针的方法进行遍历，不能用dp是因为符合重复问题，但是不满足子问题
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            # 加之前还需要判断一下当前元素和前一个元素是否相同
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left_size = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > left_size:
                    right -= 1
                elif nums[left] + nums[right] < left_size:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 如果有相同的元素则会造成重复 左右区间去重
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
        

if __name__ == '__main__':
    result = Solution().threeSum([2, 0, 0, -2, -2])
    print(result)