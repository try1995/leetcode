class Solution:
    # 递归方法
    def subsets(self, nums):
        res = []
        nums = list(set(nums))

        def dfs(path, n):
            res.append(path)
            for i in nums[n:]:
                n += 1
                dfs(path + [i], n)
        dfs([], 0)
        return res

    # 迭代方法
    # def subsets(self, nums):
    #     nums = list(set(nums))
    #
    #     res = [[]]
    #     for i in nums:
    #         res = res + [[i] + num for num in res]
    #     return res


s = Solution()
print(s.subsets([1,1,2,3]))
