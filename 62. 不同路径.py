import math

class Solution(object):
    count = 0

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        思路，起始位置只能向下和向右走，这就是一个二叉树，到n或者m为0就只能沿一个方向走了，叶子节点数量就是答案
        """
        # python3.8排列组合函数
        #return comb(m+n-2, n-1)


s = Solution()
data = s.uniquePaths(23,12 )
print(data)
