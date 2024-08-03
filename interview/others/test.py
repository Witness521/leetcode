'''
今年春季，塔子哥幼儿园开课了。开春小朋友入学报名参加互联网各大厂的春招。小朋友都排好队。但小朋友的身高有
高有低，所以塔老师让所有小朋友报数：以自身为基准向队尾看，有几个比自己矮的小朋友就报几
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length1 = len(num1); length2 = len(num2); carry = 0
        min_length = min(length1, length2)
        num1 = num1[::-1]
        num2 = num2[::-1]

        result = ''
        for i in range(min_length):
            total = int(num1[i]) + int(num2[i]) + carry
            carry = 0
            if total > 9:
                carry = 1
            total = total % 10
            result += str(total)
        if min_length < length1:
            for i in range(min_length, length1):
                total = int(num1[i]) + carry
                carry = 0
                if total > 9:
                    carry = 1
                    total = total % 10
                    result += str(total)
        elif min_length < length2:
            for i in range(min_length, length2):
                total = int(num2[i]) + carry
                carry = 0
                if total > 9:
                    carry = 1
                total = total % 10
                result += str(total)
        
        if carry == 1:
            result += '1'
        result = result[::-1]
        return result
    

            
            
if __name__ == '__main__':
    re = Solution().addStrings(num1 = "11", num2 = "123")
    print(re)