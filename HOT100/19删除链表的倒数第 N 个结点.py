'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 统计链表的长度
        listLen = 0
        head_pointer = head
        while head_pointer:
            listLen += 1
            head_pointer = head_pointer.next
        '''添加哑节点，解决头节点没有前驱节点的问题'''
        dummy = ListNode(0, head)  # 为头节点添加哑节点
        head_pointer = dummy
        # 快慢指针解决问题
        for _ in range(listLen - n):
            head_pointer = head_pointer.next
        head_pointer.next = head_pointer.next.next
        return head

