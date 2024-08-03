# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# 示例:

# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL




# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

# # 链表反转
# def reverse(node: ListNode):
#     pre = None
#     while node:
#         next1 = node.next
#         node.next = pre
#         pre = node
#         node = next1
#     return pre


# # 查询m和n的位置
# def searchMN(node: ListNode, m, n):
#     dummy = ListNode(0, node)

#     pre = dummy
#     mNode = None
#     for i in range(n):
#         if i == m-1:
#             mNode = pre
#         pre = pre.next
#     # pre是n的位置
#     head = mNode.next
#     mNode.next = None
#     tail = pre.next
#     pre.next = None
    
#     newHead = reverse(head)
#     mNode.next = newHead
#     while newHead.next:
#         newHead = newHead.next
    
#     newHead.next = tail
#     return dummy.next

# def main():
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(3)
#     node4 = ListNode(4)
#     node5 = ListNode(5)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = None

#     node = searchMN(node1, 2, 4)

#     # node = reverse(node1)
#     while node:
#         print(node.val)
#         node = node.next

# main()


class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    def reverse(self, head: LinkedNode):
        pre = None
        node = head
        while node:
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        return pre

    def reorderList(self, head: LinkedNode):
        # 快慢指针找链表的中点
        slow = head
        fast = head.next
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        backNodes = slow.next  # 后续需要反转的链表
        reverseHead = self.reverse(backNodes)
        p1 = head  # 指针指向头
        while reverseHead:
            p2 = reverseHead.next  # 记录reverseHead的下一个
            reverseHead.next = p1.next
            p1.next = reverseHead
            p1 = p1.next
            if p1:
                p1 = p1.next
            
            # 更新reverseHead  (忘记了)
            reverseHead = p2

if __name__ == '__main__':
    LinkedNode(val=0)

















# package main
# import fmt "fmt"

# func main() {
#      fmt.Printf("Hello, World!");
# }

# func TestSlice(t *testing.T) {
# 	a := []int{1, 2, 3}
# 	t.Log(a)
# 	f2(a)
# 	t.Log(a)
# }

# type SliceHeader struct {
#     Data uintptr
#     Len int
#     Cap int
# }

# func f1(a []int) {
# 	a[0] = 10
# }

# func f2(a []int) {
# 	a = append(a, 10)
# }





# func TestDefer(t *testing.T) {
# 	t1 := time.Now()
# 	defer fmt.Printf("use time: %+v", time.Now().Sub(t1))

#     // 业务代码
# 	time.Sleep(3 * time.Second)
# }

if __name__ == '__main__':
