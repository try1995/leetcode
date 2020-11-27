class Solution(object):
    def maximumGap(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums < 2:
            return 0
        nums.sort()
        ls = []
        for i in range(len_nums - 1):
            ls.append(nums[i+1] - nums[i])
        return max(ls)


s = Solution()
data = s.maximumGap([2,99999999])
print(data)
