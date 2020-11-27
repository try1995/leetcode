# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def ofs(root_):
            if not root_:
                return
            ofs(root_.left)
            res.append(root_.val)
            ofs(root_.right)

        ofs(root)
        return res


# 栈方法
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        path = []
        res = [root.val]

        def ofs(T):
            if T.left:
                res.append(T.left.val)
                ofs(T.left)
            if T.right:
                path.append(res.pop(-1))
                res.append(T.right.val)
                ofs(T.right)
            else:
                path.append(res.pop(-1))
                return path

        ofs(root)
        return path
'''

T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T5 = TreeNode(5)
T1.left = T2
T1.right = T3
T2.left = T5


s = Solution()
print(s.inorderTraversal(T1))
