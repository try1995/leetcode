class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        思路，起始位置只能向下和向右走，这就是一个二叉树，到n或者m为0就只能沿一个方向走了，叶子节点数量就是答案
        """
        count = 0

        # POINT = point(m, n)
        def helper(m_, n_):
            nonlocal count
            if m_ == 0 or n_ == 0:
                count += 1
                return
            count += m_
            helper(m_-1, n_)
        helper(m, n)
        return count


s = Solution()
data = s.uniquePaths(3,3)
print(data)
