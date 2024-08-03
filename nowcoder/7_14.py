import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    # 朴素思想：将所有链表的第一个节点放入最小堆中，取出第一个之后，指针移动，放入第二个
    def mergeKLists(self, lists) -> ListNode:
        def __lt__(a: ListNode, b: ListNode):
            return a.val < b.val
        ListNode.__lt__ = __lt__
        
        if not lists: return None
        heap = []
        dummy = ListNode()
        pointer = dummy
        for l in lists:
            if l:
                heap.append(l)
        
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            pointer.next = node
            pointer = pointer.next

            if node.next:
                heapq.heappush(heap, node.next)
            # 切断之前的联系
            node.next = None
        
        return dummy.next

if __name__ == '__main__':
    lists = []
    node2=ListNode(2)
    node1 = ListNode(1, next=node2)

    lists.append(node1)

    node3 = ListNode(3)
    lists.append(node3)
    node = Solution().mergeKLists(lists)
    print(node.val)