
class BinHeap:
    def __init__(self):
        self.currentSize = 0
        self.heapList = None
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    # 小根堆 从i向下找比i小的元素交换
    def percDown(self, i):
        # 如果左子树存在
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]
            i = mc


    # 求左右子树中最小的
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2+1] > self.heapList[i*2]:
                return i * 2
            else:
                return i * 2 + 1

if __name__ == '__main__':
    BH = BinHeap()
    BH.buildHeap([9, 6, 5, 2, 3])
    print(BH.heapList)