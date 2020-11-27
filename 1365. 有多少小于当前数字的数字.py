class Solution:
    def smallerNumbersThanCurrent(self, nums:list):
        sort_ls = sorted(nums)
        ls = []
        for i in nums:
            ls.append(sort_ls.index(i))
        return ls


s = Solution()
data = s.smallerNumbersThanCurrent(nums = [7,7,7])
print(data)