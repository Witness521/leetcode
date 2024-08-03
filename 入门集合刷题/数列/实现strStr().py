class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is "":
            return 0
        if haystack is "":
            return -1
        i = 0
        while i < len(haystack)-len(needle)+1:  # 遍历源字符串
            save_i = i  # 防止因为比对造成haystack的索引移动
            j = 0
            while haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return i - j
                j += 1
                i += 1
            i = save_i + 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("mississippi", "issip"))
