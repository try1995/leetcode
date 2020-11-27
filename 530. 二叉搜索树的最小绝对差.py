# Definition for a binary tree node.
from leetcode.tool import *
import sys


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ls = []
        int_max = sys.maxsize
        def DFS(Tree):
            if not Tree:
                return
            DFS(Tree.left)
            ls.append(Tree.val)
            DFS(Tree.right)
        DFS(root)
        diz = int_max
        for i in range(len(ls) - 1):
            dff = abs(ls[i] - ls[i+1])
            if dff < diz:
                diz = dff
        return diz

s = Solution()
data = s.getMinimumDifference(convert_list_to_tree([236,104,701,None,227,None,911]))
print(data)

