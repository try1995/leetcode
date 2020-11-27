# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.tool import *


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ls = []

        def helper(root_, ls_):
            if root_.left is None and root_.right is None:
                ls.append(int("".join([str(i) for i in ls_])))
                return
            if root_.left:
                helper(root_.left, ls_ + [root_.left.val])
            if root_.right:
                helper(root_.right, ls_ + [root_.right.val])

        helper(root, [root.val])

        return sum(ls)


s = Solution()
# data = s.sumNumbers(convert_list_to_tree([1,2,3]))
l1 = TreeNode(0)
l1.left = TreeNode(1)
data = s.sumNumbers(l1)
print(data)
