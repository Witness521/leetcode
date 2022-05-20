'''
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
'''
class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 0
        memo[1] = 1
        def func(n: int):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if memo[n] != 0:
                return memo[n]
            memo[n] = func(n - 1) + func(n - 2)
            return memo[n]
        return func(n)

if __name__ == '__main__':
    print(Solution().fib(3))