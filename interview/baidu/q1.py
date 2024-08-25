

class DlinkedNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
    
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            # 取出node
            node.prev.next = node.next
            node.next.prev = node.prev
            # 插入链表头
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next.prev = node
            return node.val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            # 取出node
            node.prev.next = node.next
            node.next.prev = node.prev
            # 插入链表头
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next.prev = node
            
            node.val = value
            self.hashmap[key] = node
        else:
            if len(self.hashmap) >= self.capacity:
                lastNode = self.tail.prev
                del self.hashmap[lastNode.val]
                lastNode.prev.next = self.tail
                self.tail.prev = lastNode.prev

            node = DlinkedNode(value)
            self.hashmap[key] = node
            # 插入链表头
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next.prev = node

lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))