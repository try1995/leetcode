# Definition for a Node.
from leetcode.tool import *
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        begin = root
        queue = deque([root])
        while queue:
            size = len(queue)
            # temp保存了每一层的node节点
            temp = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node)
                if i < size -1:
                    node.next = queue[0]
        return begin


