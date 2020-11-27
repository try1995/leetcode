# Definition for singly-linked list.
from leetcode.tool import *


# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        ls = [head]

        while head.next:
            ls.append(head.next)
            head = head.next
        head = ls[0]
        n = len(ls) - 1
        i = 0
        j = 0
        while True:
            if n - j == j:
                head.next = ls[j]
                ls[j].next = None
                break
            if i == n:
                ls[n-j+1].next = None
                break
            if i % 2 == 1:
                head.next = ls[j]
            else:
                head.next = ls[n - j]
                j += 1
            head = head.next
            i += 1
        return ls[0]


l0 = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
# l4 = ListNode(5)
l0.next = l1
l1.next = l2
l2.next = l3
# l3.next = l4
s = Solution()

data = s.reorderList(l0)
# data = l0
while data:
    print(data.val)
    data = data.next

