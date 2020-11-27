class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_set = set(nums)
        dict_k = {str(i): 0 for i in nums_set}
        for i in nums:
            dict_k[str(i)] += 1
        k_sort = sorted(dict_k.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        k_sort = k_sort[:k]
        ls = [int(i[0]) for i in k_sort]
        return ls


s = Solution()
data = s.topKFrequent([1], 1)
print(data)

