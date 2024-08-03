
s = '1379610'
list_num = []

for c in s:
    list_num.append(int(c))

# 滑动窗口 偏暴力的方法
# left = 0
# right = 1
# while right < len(list_num):
#     if list_num[left] + list_num[right] == 10:
#         list_num.pop(left)
#         list_num.pop(left)
#         left = 0
#         right = 1
#         continue
    
#     left+=1; right+=1

# print(list_num)

# 使用栈的方法

stack = []
for num in list_num:
    if stack:
        top = stack[-1]
        if num + top == 10:
            stack.pop()
            continue

    stack.append(num)


print(stack)
print(len(stack))
