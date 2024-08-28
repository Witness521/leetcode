class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# k个节点一组，逆转单链表
# @param head ListNode类  头节点
# @param k int整型  组大小
# @return ListNode类
#
class Solution:
    def revertLinkList(self, head, k) :
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node:
            pre = node
            for _ in range(k):
                if node.next is None:
                    return dummy.next
                node = node.next
            temp = node.next
            node.next = None
            reverseHead = pre.next
            pre.next = None  # 断开
            newHead = self.reverse(reverseHead)
            pre.next = newHead
            # 找反转的尾部
            while newHead.next:
                newHead = newHead.next
            newHead.next = temp
            pre = newHead
            node = newHead
        return dummy.next

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    head = Solution().revertLinkList(node1, 1)
    while head:
        print(head.val)
        head = head.next