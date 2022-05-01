'''设计实现双端队列。'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k  # 设置k个位置
        self.cir_queue = [0] * self.size
        self.head = self.rear = 0

    def insertFront(self, value: int) -> bool:


    def insertLast(self, value: int) -> bool:


    def deleteFront(self) -> bool:


    def deleteLast(self) -> bool:


    def getFront(self) -> int:


    def getRear(self) -> int:


    def isEmpty(self) -> bool:
        if self.head == self.rear:


    def isFull(self) -> bool: