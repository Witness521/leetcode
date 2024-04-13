# 对一个字符串中的所有字符排列组合出他们所有的大小写可能性
# 例如a1b2 输出["A1b2", "A1B2", "a1b2", "a1B2"]

class Solution:
    def __init__(self) -> None:
        self.result = []
    
    def combine(self, str1: str, index: int, path: list):
        if index == len(str1):
            self.result.append(''.join(path))
            return
        
        if str1[index].isalpha():
            if ord(str1[index]) in range(ord('A'), ord('Z')+1):
                path.append(str1[index])
                self.combine(str1, index+1, path)
                # 回溯
                path.pop()

                path.append(str1[index].lower())
                self.combine(str1, index+1, path)
                path.pop()
            else:  # 小写字母
                path.append(str1[index])
                self.combine(str1, index+1, path)
                # 回溯
                path.pop()

                path.append(str1[index].upper())
                self.combine(str1, index+1, path)
                path.pop()

            
        else:  # 不是字符 是数字
            path.append(str1[index])
            self.combine(str1, index+1, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    s.combine("a1b2", 0, [])
    print(s.result)