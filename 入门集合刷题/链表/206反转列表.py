'''给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head == []:
            return head
        prev = head
        cur = None
        while prev:
            # 保存prev的next
            save = prev.next
            prev.next = cur
            cur = prev
            prev = save
        return cur

if __name__ == '__main__':
    print(Solution().reverseList([]))

