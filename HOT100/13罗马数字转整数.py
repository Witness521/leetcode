class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        if len(s) == 1:
            return hashmap[s]
        else:
            total = 0
            for i in range(1, len(s)):
                right = s[i]
                left = s[i - 1]
                if hashmap[left] < hashmap[right]:
                    total -= hashmap[left]
                else:
                    total += hashmap[left]
            total += hashmap[s[-1]]
        return total





if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))