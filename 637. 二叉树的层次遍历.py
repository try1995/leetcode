class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                temp.append(queue.pop(0).val)
            res.append(temp)
        return res


T1 = TreeNode(3)
T2 = TreeNode(9)
T3 = TreeNode(20)
T4 = TreeNode(15)
T5 = TreeNode(7)
T1.left = T2
T1.right = T3
T3.left = T4
T3.right = T5

s = Solution()
print(s.averageOfLevels(T1))

