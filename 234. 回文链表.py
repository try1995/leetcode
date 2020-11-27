# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.tool import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return None
        ls_head = []
        while head:
            ls_head.append(head.val)
            head = head.next
        i = 0
        j = len(ls_head) - 1
        while i < j:
            if ls_head[i] != ls_head[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(2)
L4 = ListNode(1)
L1.next = L2
L2.next = L3
L3.next = L4
s = Solution()
data = s.isPalindrome(L1)
print(data)
