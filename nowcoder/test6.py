class Solution:
    def reorderList(self , head ):
        dummy = ListNode(0)
        dummy.next = head
        # 快慢指针找中点
        slow, fast = dummy, head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        reverseHead = slow.next
        slow.next = None
        newHead = self.reverse(reverseHead)
        while head and newHead:
            temp = newHead.next
            newHead.next = head.next
            head.next = newHead
            head = newHead.next
            newHead = temp
        return dummy.next

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre