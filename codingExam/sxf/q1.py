
color = input()
command = input()

# i = 0
# prevCommand = command[0]
# j = 0

# while j < len(color) and i < len(command):
#     if color[j] == command[i]:
#         prevCommand = command[i]
#         i += 1
#         j += 1
#     elif command[i] == '*':
#         while prevCommand == color[j]:
#             j += 1
#         i += 1
#     else:
#         break
# print(j)
def is_match(s: str, p: str) -> int:
    i, j = 0, 0
    match = 0
    star_index = -1

    while i < len(s):
        # 如果字符匹配，或者模式字符是 '.'
        if j < len(p) and (p[j] == s[i] or p[j] == '.'):
            i += 1
            j += 1
        # 如果模式字符是 '*'，记录 '*' 位置和当前字符串的位置
        elif j < len(p) and p[j] == '*':
            star_index = j
            match = i
            j += 1
        # 如果之前有 '*'，尝试匹配更多字符
        elif star_index != -1:
            j = star_index + 1
            match += 1
            i = match
        # 无法匹配
        else:
            return 0

    # 检查剩余的模式字符是否都是 '*'（可以匹配0个字符）
    while j < len(p) and p[j] == '*':
        j += 1

    return i if j == len(p) else 0

print(is_match(color, command))














