

class Solution:
    def findClosetPair(self, arr1, arr2, x) :
        arr1.sort()
        arr2.sort()
        # arr1从小往大找 arr2从大往小找
        i1, i2 = 0, len(arr2)-1
        minNum = 1e6
        result = []
        while i1 < len(arr1) and i2 >= 0:
            re = arr1[i1] + arr2[i2]
            if minNum > abs(re - x):
                result = [i1, i2]
            if re > x:
                i2 -= 1
            elif re < x:
                i1 += 1
            else:
                return result
        return result
    
if __name__ == '__main__':
    print(Solution().findClosetPair([1,5,13,15],[10,11,17,20],20))
            