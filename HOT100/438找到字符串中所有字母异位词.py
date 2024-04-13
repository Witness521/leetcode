from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口的思想
        s_list = [0] * 26
        p_list = [0] * 26
        count = []
        # 使用数组保存两个滑动窗口内部的元素
        for c in p:
            p_list[ord(c) - ord('a')] += 1
        left = 0; right = len(p) - 1
        for c in s[left : right+1]:  # 取right
            s_list[ord(c) - ord('a')] += 1

        # 
        while right < len(s):
            if s_list == p_list:
                count.append(left)
            # 向右移动窗口
            s_list[ord(s[left]) - ord('a')] -= 1
            right += 1; left += 1
            if right < len(s):
                # 此处是index需要减一
                s_list[ord(s[right]) - ord('a')] += 1

        return count


if __name__ == '__main__':
    ans = Solution().findAnagrams(s = "cbaebabacd", p = "abc")
    print(ans)