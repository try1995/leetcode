# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode):
        if not head:
            return None
        if head and not head.next:
            return "no cycle"
        turtle = head.next
        rabit = head.next.next
        while True:
            if not rabit or not rabit.next:
                return "no cycle"
            turtle = turtle.next
            rabit = rabit.next.next
            if turtle == rabit:
                count = 0
                ptr = head
                while ptr!= turtle:
                    ptr = ptr.next
                    turtle = turtle.next
                    count += 1
                return "tail connects to node index %s"%count


lz = ListNode(1)
L0 = ListNode(3)
L1 = ListNode(2)
L2 = ListNode(0)
L3 = ListNode(4)
lz.next = L0
L0.next = L1
L1.next = L2
L2.next = L3
L3.next = L1


s = Solution()
data = s.hasCycle(lz)
print(data)
