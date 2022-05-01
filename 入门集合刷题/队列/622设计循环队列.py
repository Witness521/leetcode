'''设计你的循环队列实现。 循环队列是一种线性数据结构，
其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1  # 设置k+1个位置
        self.cir_queue = [0] * self.size
        self.head = self.rear = 0

    def enQueue(self, value: int) -> bool:
        # 如果循环队列满了
        if self.isFull():
            return False
        # 在rear的位置放置元素
        self.cir_queue[self.rear] = value
        # rear向后移动一位
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cir_queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cir_queue[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        if self.head == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.head:
            return True
        return False

if __name__ == '__main__':
# Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(5)
    param_1 = obj.enQueue(1)
    print(param_1)
    param_2 = obj.deQueue()

    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()