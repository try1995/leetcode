# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.tool import *


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ls = []
        queue = [[root]]
        count = 0
        while queue:
            nodes = queue.pop(0)
            temp = []
            temp2 = []
            for node in nodes:
                temp2.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                queue.append(temp)
            # 必须在外面
            count += 1
            if count % 2 == 0:
                temp2.reverse()
            ls.append(temp2)
        return ls


if __name__ == '__main__':
    root = convert_list_to_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    ret = s.levelOrder(root)
    print(ret)
