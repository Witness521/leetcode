# 给定一个单向链表，判断链表中是否有环，如果链表中有某个节点，可以通过连续跟踪next指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。如果pos是-1，则在该链表中没有环。
# 注意：pos不作为参数进行传递，仅仅是为了标识链表的实际情况。如果链表中存在环，则返回true；否则返回false。
# 例如：
# 输入：list=[5,8,9,2,3],pos=1，输出:true
# 输入：list=[1,2],pos=0，输出:true
# 输入：list=[2,3],pos=-1，输出:false

# 定义：
# //Definition for singly-linked list.
# public class ListNode {
#     int val;
#     ListNode next;
#     ListNode(int x) {
#         val = x;
#         next = null;
#     }
# }

class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None
    
def isCircle(node: ListNode):  # 快慢指针解决问题
    if node is None:
        return False
    slow = node
    fast = node.next
    while slow and fast:
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return False

if __name__ == "__main__":
    dummy = ListNode(0)
    node = ListNode(5)
    dummy.next = node

    node.next = ListNode(8)
    node = node.next
    node.next = ListNode(9)
    node = node.next
    node.next = dummy.next

    print(isCircle(dummy.next))

