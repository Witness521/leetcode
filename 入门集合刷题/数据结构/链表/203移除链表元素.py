'''
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return []
        if head == []:
            return []
        # 找寻head的位置
        while head.val == val:
            head = head.next
        # 删除链表头后面的val
        pointer = head
        while pointer.next:
            # pointer的下一个node的值为val
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head

if __name__ == '__main__':
    print(Solution().removeElements([], 1))