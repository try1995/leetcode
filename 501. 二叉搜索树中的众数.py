# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode):
        if not root:
            return []
        res = {}

        def RDL(root):
            if not root:
                return
            RDL(root.left)
            res[root.val] = res.get(root.val, 0) + 1
            RDL(root.right)

        RDL(root)
        max_value = max(res.values())
        return [key for key, value in res.items() if value == max_value]


T1 = TreeNode(1)
T1.right = TreeNode(2)
T1.right.left = TreeNode(2)
s = Solution()
data = s.findMode(T1)
print(data)
