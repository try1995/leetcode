class Solution(object):
    def searchRange(self, nums:list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        try:
            left = nums.index(target)
            right = left
            while True:
                if right+1 == len(nums):
                    break
                if nums[right+1] == target:
                    right += 1
                else:
                    break
            return [left, right]
        except:
            return [-1, -1]


s = Solution()
data = s.searchRange(nums = [1], target = 1)
print(data)