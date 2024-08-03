
nums = [2,5,4,1,8]

# 从小到大
for i in range(1, len(nums)):
    num = nums[i]
    for j in range(i-1, -1, -1):
        if nums[j] > num:
            nums[j+1], nums[j] = nums[j], nums[j+1]
        else:
            break
    
print(nums)
        
    

