class Solution(object):
    def moveZeroes(self, nums: list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)
        print(nums)


s = Solution()
data = s.moveZeroes([0,1,0,3,12])
print(data)

