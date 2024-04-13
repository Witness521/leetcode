'''
请你设计并实现一个满足LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字key 已经存在，则变更其数据值value ；如果不存在，则向缓存中插入该组key-value 。
如果插入操作导致关键字数量超过capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
'''
class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    '''
        数据结构：
        dict中保存的是<key, 链表节点的指针>
        链表是双向链表 使用于添加和删除节点
    '''
    def __init__(self, capacity: int):
        self.hashset = {}  # 设置一个字典保存<key, 链表节点的指针>
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove_and_insert(self, key):
        node = self.hashset[key]
        # 从列表中抽离出来
        node.pre.next = node.next
        node.next.pre = node.pre
        # 从队尾插入
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.hashset:
            self.remove_and_insert(key)
            node = self.hashset[key]
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hashset:
            if self.capacity == len(self.hashset):
                # 删除老的元素
                self.hashset.pop(self.head.next.key)
                # 删除队头的元素
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            # 从队尾入队
            new_node = DLinkedNode(key, value)
            self.hashset[key] = new_node
            self.tail.pre.next = new_node
            new_node.pre = self.tail.pre
            new_node.next = self.tail
            self.tail.pre = new_node
        else: # key在链表中
            self.remove_and_insert(key)





if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.get(2))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)