class Solution(object):
    def combinationSum(self, candidates: list, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(n, index):
            print(index)
            adds = sum(n)
            if adds == target:
                res.append(n)
                return
            # 剪枝,差值比候选的最小的还要小，说明加上最小的就超过target
            if target - adds < min(candidates[index:]):
                return
            for j in candidates[index:]:
                dfs(n + [j], index)
                index += 1

        dfs([], 0)
        return res


s = Solution()
data = s.combinationSum(candidates=[2, 3, 5], target=8)
print(data)
