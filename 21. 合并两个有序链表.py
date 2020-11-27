# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.tool import *

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        heard = ListNode()
        l = heard
        while l1 or l2:
            if not l1:
                l.next = l2
                break
            if not l2:
                l.next = l1
                break
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        return heard.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l1.next = l2
l2.next = l3

l4.next = l5
l5.next = l6
s = Solution()
data = s.mergeTwoLists(l1, l4)
print(data)