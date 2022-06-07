'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        pointer = new_list
        pointer1 = list1
        pointer2 = list2
        while pointer1 and pointer2:
            if pointer1.val > pointer2.val:
                pointer.next = pointer2
                pointer2 = pointer2.next
            else:
                pointer.next = pointer1
                pointer1 = pointer1.next
            pointer = pointer.next  # 指针后移
        if pointer1:  # pointer1未空
            pointer.next = pointer1
        elif pointer2:  # pointer2未空
            pointer.next = pointer2
        return new_list.next


