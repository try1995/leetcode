class node:
    def __init__(self, next_item, pre_item, val):
        self.next = next_item
        self.prior = pre_item
        self.val = val


class Solution(object):
    def convert(self, ring, key):
        ls_ring = list(ring)
        len_ring = len(ring)
        head = node(None, None, ls_ring[0])
        ls_node = []
        for item in ls_ring:
            ls_node.append(node(None, None, item))
        for index, item in enumerate(ls_ring):
            pre_index = (index - 1 + len_ring) // len_ring
            next_index = (index + 1 + len_ring) // len_ring
            node(ls_ring[next_index], ls_ring[pre_index], item)

    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        pass


s = Solution()
data =
