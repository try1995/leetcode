class Solution:
    def twoSum(self, nums, target: int):
        dct = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in dct:
                return [dct[t], i]
            else:
                dct[n] = i


s = Solution()
data = s.twoSum(nums = [3,2,4], target = 6)
print(data)

