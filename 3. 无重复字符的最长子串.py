class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            i = len(set(s))
            if i == len(s):
                return i
            while i:
                for j in range(len(s) - i + 1):
                    if len(s[j:j+i]) == len(set(s[j:j+i])):
                        return i
                i -= 1
        return 0


s = Solution()
print(s.lengthOfLongestSubstring("au"))
