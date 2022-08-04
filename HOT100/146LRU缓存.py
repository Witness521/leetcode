'''
请你设计并实现一个满足LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字key 已经存在，则变更其数据值value ；如果不存在，则向缓存中插入该组key-value 。
如果插入操作导致关键字数量超过capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
'''
class ListNode:
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
        self.dict1 = {}  # 设置一个字典保存<key, 链表节点的指针>
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_tail(self, node):
        # 将node放到尾节点之前
        # 将node解出来
        node.pre.next = node.next
        node.next.pre = node.pre
        # 将node放到尾节点之前
        self.tail.pre.next = node
        node.next = self.tail
        node.pre = self.tail.pre
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.dict1.keys():
            node = self.dict1[key]
            self.move_node_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict1.keys():
            # 获取到key对应节点的地址
            node = self.dict1[key]
            node.value = value
            self.move_node_to_tail(node)
        else:
            if self.capacity == len(self.dict1):
                # 去掉最前面的节点
                self.dict1.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head

            node = ListNode(key, value)
            # 将node放到列表的尾部
            self.tail.pre.next = node
            node.next = self.tail
            node.pre = self.tail.pre
            self.tail.pre = node
            # 将新的节点储存到dict中
            self.dict1[key] = node

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