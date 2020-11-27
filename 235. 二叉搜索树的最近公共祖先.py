from leetcode.tool import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root):
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


Tree = convert_list_to_tree([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, None, None, None])
s = Solution()
data = s.lowestCommonAncestor(Tree, TreeNode(1), TreeNode(3))
print(data.val)
