# 判断素数 要求程序的时间复杂度小于根号N

"""
k 执行k次测试
"""
import random

class Solution:
    def isPrimeNumberByMR(self, n: int, k: int):
        # 使用Miller-Rabin素数测试算法
        if n <= 1:
            return False
        elif n == 2 or n == 3:
            return True
        # 将n-1表示为2 ^ r * d的形式
        r = 1
        while 1:
            d = (n - 1) / pow(2, r)
            if d % 2:
                break
            else:
                r += 1
        for _ in range(k):
            a = random.randint(2, n-2)
            x = self.quick_pow(a, d, n)  # 优化
            if x == 1 or x == n-1:
                continue
            for _ in range(r-1):
                x = self.quick_pow(x, 2, n)
                if x == n-1:
                    break
            else:
                return False
        return True

    def quick_pow(self, a, d, n):
        ans = 1
        while d:
            ans = ans * a % n
            a = a * a % n
            d = d // 2
        return ans

if __name__ == '__main__':
    S = Solution()
    print("509 is Prime Number ? ", S.isPrimeNumberByMR(509, 20))
    print("20 is Prime Number ? ", S.isPrimeNumberByMR(20, 20))
    print("7 is Prime Number ? ", S.isPrimeNumberByMR(7, 20))
