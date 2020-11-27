class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        # 遍历左子树
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + i)
        return paths





