from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count_arr = Counter(arr)
        return len(count_arr.values()) == len(set(count_arr.values()))


s = Solution()
data = s.uniqueOccurrences([1,2,2,1,1,3,3])
print(data)