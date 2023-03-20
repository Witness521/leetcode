'''
    给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(next=head)
        length = 0  # 计算链表的长度
        p = head
        while p:
            length += 1
            p = p.next

        size = 1
        while size < length:
            cur = dummyNode.next
            tail = dummyNode
            while cur:
                left = cur
                right = self.cut(left, size)
                cur = self.cut(right, size)
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            size = size * 2
        return dummyNode.next


    # 将链表l切掉前n个节点
    def cut(self, l: ListNode, n: int):
        temp = l
        while n > 1 and temp:
            temp = temp.next
            n -= 1
        if not temp:
            return None
        next = temp.next
        temp.next = None
        return next


    # 双路归并
    def merge(self, l1: ListNode, l2: ListNode):
        dummyNode = ListNode()
        pointer = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                pointer = l1
                l1 = l1.next
            else:  # l1.val > l2.val
                pointer.next = l2
                pointer = l2
                l2 = l2.next
        pointer.next = l1 if l1 else l2
        return dummyNode.next



