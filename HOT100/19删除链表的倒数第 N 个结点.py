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
        '''中心思想：添加哑节点 就不会出现首节点前驱的糟心事'''

        # 1. 统计链表的长度
        # listLen = 0
        # head_pointer = head
        # while head_pointer:
        #     listLen += 1
        #     head_pointer = head_pointer.next
        # '''添加哑节点，解决头节点没有前驱节点的问题'''
        # dummy = ListNode(0, head)  # 为头节点添加哑节点
        # head_pointer = dummy
        # # 快慢指针解决问题
        # for _ in range(listLen - n):
        #     head_pointer = head_pointer.next
        # head_pointer.next = head_pointer.next.next
        # return head

        # 2. 使用栈的方法
        # dummy = ListNode(0, head)
        # head_pointer = dummy
        # stack = []
        # while head_pointer:
        #     stack.append(head_pointer)
        #     head_pointer = head_pointer.next
        # for i in range(n):
        #     stack.pop()
        # # 待删除元素的左元素
        # element_left = stack.pop()
        # head_pointer = dummy
        # while head_pointer != element_left:
        #     head_pointer = head_pointer.next
        # head_pointer.next = head_pointer.next.next
        # return dummy.next
        dummy = ListNode(next=head)
        stack = []
        rear = None
        pointer = dummy
        while pointer:
            stack.append(pointer)
            pointer = pointer.next
        if len(stack) == 2:
            return None
        for i in range(n-1):  # 删除后n-1个节点
            rear = stack.pop()
        stack.pop()
        front = stack.pop()
        front.next = rear
        return dummy.next

if __name__ == '__main__':
    for i in range(-1):
        print(i)
