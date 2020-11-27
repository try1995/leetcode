# refer to https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if (k < 0) | (k > n):
            return []

        def dfs(ret, j):
            if len(ret) == k:
                res.append(ret)
                return

            for i in range(j + 1, n + 1):
                # 剪枝
                if i <= (n - (k - len(ret)) + 1):
                    dfs(ret + [i], i)

        res = []
        dfs([], 0)
        return res


s = Solution()
data = s.combine(4, 2)
print(data)
