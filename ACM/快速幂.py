# n k
# n个数
# q个数字 q行


def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n < 0:
        n = abs(n)
        x = 1 / x
    if n % 2:  # 如果n是奇数
        re = myPow(x, (n-1) / 2)
        return re * re * x
    else:  # 偶数
        re = myPow(x, n / 2)
        return re * re
            
# print(Solution().myPow(2.0, -2))

if __name__ == '__main__':
    line1 = input()
    n, q = line1.split(' '); n, q = int(n), int(q)
    line2 = input()
    n_list = line2.split(' '); n_list = [int(_) for _ in n_list]
    q_list = []
    for _ in range(q):
        q_i = int(input())
        q_list.append(q_i)

    times = [q] * n
    for q_i in q_list:
        i = n_list.index(q_i)
        times[i] -= 1

    mod = 1e9 + 7
    result = 0
    for i in range(len(n_list)):
        time = myPow(2, times[i]) % mod
        result += time * n_list[i] % mod
        result = result % mod
    print(result)

