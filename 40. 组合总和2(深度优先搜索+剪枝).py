class Solution(object):
    def combinationSum(self, candidates: list, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(n, target_, index):
            if 0 == target_:
                n.sort()
                if n not in res:
                    res.append(n)
                    return
            cut_ls = []
            for i in candidates[index:]:
                index += 1
                if target_ - i < 0:
                    break
                if i not in cut_ls:
                    cut_ls.append(i)
                    dfs(n + [i], target_ - i, index)

        dfs([], target, 0)
        return res


s = Solution()
data = s.combinationSum(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
print(data)
