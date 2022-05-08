'''设计实现双端队列。'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k + 1
        self.cir_queue = [0] * self.size
        self.head = self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.size) % self.size
        self.cir_queue[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cir_queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.cir_queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cir_queue[(self.rear-1+self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.head == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.head