'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        currentCur = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            remainder = (val1 + val2 + carry) % 10  # 余数
            carry = (val1 + val2 + carry) // 10  # 进位
            currentCur.next = ListNode(remainder)
            currentCur = currentCur.next
        return head.next

if __name__ == '__main__':
    print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))


