#  已知一个int数组，输出所有升序子集

nums = [1,2,3,4]

result = []
def dfs(nums, re, j):
    result.append(re.copy())

    for i in range(j, len(nums)):
        re.append(nums[i])
        dfs(nums, re, i+1)
        re.pop()

def permute(nums, start, end):
    

dfs(nums, [], 0)
print(result)