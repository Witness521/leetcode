'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 设置一个长度为lists.len的数组存放当前的 "首元素"
        first_node = [0 * len(lists)]
        result = ListNode(0, None)
        index = 0
        # 初始化first_node列表
        for list in lists:
            first_node[index] = list.val
            index += 1

        count = 0
        if count < len(lists):
            node_val = min(first_node)
            result.next = ListNode(node_val)
            # 找到第几个list的节点
            list_index = first_node.index(min(first_node))
            # 对应的list向下移动一个节点
            lists[list_index] = lists[list_index].next
            if lists[list_index] is None:
                count += 1
                first_node[list_index] = -10^4
            else:
                # 更新first_node中的值
                first_node[list_index] = lists[list_index].val

        return result


if __name__ == '__main__':

