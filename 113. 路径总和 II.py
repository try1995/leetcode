# Definition for a binary tree node.
from leetcode.tool import *


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        if not root:
            return []
        res = []

        def helper(root_: TreeNode, path: list, adds):
            if (adds == target) & (not root_.left) & (not root_.right):
                res.append(path)
                return
            else:
                if root_.left:
                    helper(root_.left, path + [root_.left.val], adds + root_.left.val)
                if root_.right:
                    helper(root_.right, path + [root_.right.val], adds + root_.right.val)
        helper(root, [root.val], root.val)
        return res


s = Solution()
begin = TreeNode(5)
begin.left = TreeNode(4)
begin.right = TreeNode(8)
begin.left.left = TreeNode(11)
begin.right.left = TreeNode(13)
begin.right.right = TreeNode(4)
begin.left.left.left = TreeNode(7)
begin.left.left.right = TreeNode(2)
begin.right.right.left = TreeNode(5)
begin.right.right.right = TreeNode(1)
data = s.pathSum(begin, 22)
print(data)
