class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        dummy = ListNode(0, head)
        pre = dummy  # 已翻转的最后一个
        end = pre
        while end:
            # 找end
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            # 未翻转的链表头
            unReverseHead = end.next
            end.next = None
            # 待翻转的链表头
            waitReverseHead = pre.next
            pre.next = None

            node = self.reverse(waitReverseHead)
            pre.next = node
            for _ in range(k):
                pre = pre.next
            end = pre

            pre.next = unReverseHead
        
        return dummy.next

            
                

    def reverse(self, head: ListNode):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


if __name__ == "__main__":
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    node = Solution().reverseKGroup(node1, 2)
    while node:
        print(node.val)
        node = node.next