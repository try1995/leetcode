# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        # left = []
        #
        # def dfs(root_, left_leaves):
        #     if root_.left:
        #         dfs(root_.left, True)
        #     if root_.right:
        #         dfs(root_.right, False)
        #     if (not root_.left) & (not root_.right):
        #         if left_leaves:
        #             left.append(root_.val)
        # dfs(root, False)
        # return sum(left)
        sum = 0
        if root.left is not None:
           if(not root.left.right) & (not root.left.left):
                sum = root.left.val
        return sum + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)


T1 = TreeNode(0)
T2 = TreeNode(2)
T3 = TreeNode(4)
T5 = TreeNode(1)
T6 = TreeNode(3)
T7 = TreeNode(-1)
T8 = TreeNode(5)
T9 = TreeNode(1)
T10 = TreeNode(6)
T11 = TreeNode(8)
T1.left = T2
T1.right = T3
T2.left = T5
T3.left = T6
T3.right = T7
T5.left = T8
T5.right = T9
T6.right = T10
T7.right = T11

s = Solution()
print(s.sumOfLeftLeaves(T1))
