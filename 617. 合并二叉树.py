# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged

l1 = TreeNode(1)
# l1.left = TreeNode(4)
# l1.right = TreeNode(3)
# l1.left.right = TreeNode(1)

l2 = TreeNode(1)
l2.left = TreeNode(2)
# l2.right = TreeNode(4)
# l2.right.left = TreeNode(1)


s = Solution()
data = s.mergeTrees(l1, l2)
print(data)
