n = int(input())
str_list = input().split()
if n < 3: print(*str_list)
# 设置一个滑动窗口
left = 0; right = 2
while right < len(str_list):
    if str_list[left] == str_list[left + 1] and str_list[right] == str_list[left + 1]:
        for i in range(3):
            str_list.pop(left)
        left = 0; right = 2
    else:
        left += 1
        right += 1
if len(str_list) == 0: 
    print(0)

print(*str_list)