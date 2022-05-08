from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 快慢指针的方法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while not head or not head.next:  # 如果头为空
            return False
        # 设置快指针和慢指针
        fast = head.next
        slow = head
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True