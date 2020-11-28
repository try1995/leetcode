from collections import Counter


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        ret = 0
        for i in nums[::-1]:
            count[i] -= 1
            if count[i] == 0:
                count.pop(i)
            ret += sum([count[j] for j in count if i > 2*j])
        return ret

s = Solution()
data = s.reversePairs([2,4,3,5,1])
print(data)