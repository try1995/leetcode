# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = root.left
        right = root.right

        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T5 = TreeNode(5)
T1.left = T2
T1.right = T3
T2.right = T5

s = Solution()
print(s.invertTree(T1))
