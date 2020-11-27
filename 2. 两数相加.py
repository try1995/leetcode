# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: TreeNode
        :type l2: TreeNode
        :rtype: TreeNode
        """
        list1 = []
        list2 = []
        list1.append(str(l1.val))
        list2.append(str(l2.val))
        while True:
            if l1.next is not None:
                list1.append(str(l1.next.val))
                l1 = l1.next
            else:
                break
        while True:
            if l2.next is not None:
                list2.append(str(l2.next.val))
                l2 = l2.next
            else:
                break
        list1.reverse()
        list2.reverse()
        num1 = int("".join(list1))
        num2 = int("".join(list2))
        list3 = list(str(num1 + num2))
        list3.reverse()
        list3 = [int(i) for i in list3]
        if len(list3) > 1:
            L = TreeNode(list3[0])
            a = TreeNode(list3[1])
            L.next = a
            for i in list3[2:]:
                a.next = TreeNode(i)
                a = a.next
        else:
            L = TreeNode(list3[0])
        return L



l1 = TreeNode(0)
# l1.next = TreeNode(4)
# l1.next.next = TreeNode(3)
# l1.next.next.next = TreeNode(1)

l2 = TreeNode(5)
# l2.next = TreeNode(6)
# l2.next.next = TreeNode(4)
# l2.next.next.next = TreeNode(1)

s = Solution()
L = s.addTwoNumbers(l1, l2)

print(L.val)
while True:
    if L.next is not None:
        print(L.next.val)
        L = L.next
    else:
        break