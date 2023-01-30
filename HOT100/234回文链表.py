'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 使用快慢指针寻找中间节点
        fast = head
        slow = head
        while fast.next:
            fast = fast.next  # 快指针跳一次
            if fast.next:
                fast = fast.next  # 快指针跳第二次
            else:
                break
            slow = slow.next  # 慢指针跳一次

        second_part = slow.next
        slow.next = None
        second_part = self.reverse_list(second_part)
        return self.compare_list(head, second_part)


    def reverse_list(self, head: Optional[ListNode]):
        if head is None:
            return None
        prev = head
        cur = head.next
        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        # 头节点是prev
        head.next = None
        head = prev
        return head


    def compare_list(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True