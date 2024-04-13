
string = input()
count_1 = 0; count_2 = 0; count_3 = 0
for s in string: # 全大写
    if not s.isupper():
        count_1 += 1
for s in string:
    if not s.islower():
        count_2 += 1

for i in range(len(string)):
    if i == 0 and string[i].islower():
        count_3 += 1
    elif string[i].upper():
        count_3 += 1

print(min(count_1, count_2, count_3))