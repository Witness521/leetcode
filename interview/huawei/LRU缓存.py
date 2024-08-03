"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""

class DLinkedNode:
    def __init__(self, key=None, val=None) -> None:
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    # 使用双向链表+哈希表完成O(1)的时间复杂度
    # 链表使用队列的形式进行组织
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            # 将node解除出来
            node.prev.next = node.next
            node.next.prev = node.prev
            # 插入到尾节点之前
            node.prev = self.tail.prev
            self.tail.prev = node
            node.prev.next = node
            node.next = self.tail
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 插入到链表的尾部
        if key in self.hashmap:
            node = self.hashmap[key]
            # 将node解除出来
            node.prev.next = node.next
            node.next.prev = node.prev
            # 赋值
            node.val = value
            # 插入到尾节点之前
            node.prev = self.tail.prev
            self.tail.prev = node
            node.prev.next = node
            node.next = self.tail
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉链表头的节点
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = DLinkedNode(key=key, val=value)
            self.hashmap[key] = node
            # 将node插入到链表的尾部
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            node.prev.next = node
            

if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    result = lRUCache.get(2)
    print(result)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
