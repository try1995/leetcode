# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.tool import *


class Solution(object):
    def insert_node(self, header,node):
        next = header
        while next.next:
            if next.val <= node.val <= next.next.val:
                temp = next.next
                next.next = node
                node.next = temp
                return header
            next = next.next
        next.next = node
        return header

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        header = ListNode(-float("inf"))
        while head:
            header = self.insert_node(header, ListNode(head.val))
            head = head.next
        return header.next


l1 = ListNode(-1)
l2 = ListNode(5)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(0)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
s = Solution()
data = s.sortList(l1)
print(data)
