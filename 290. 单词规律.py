class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ls = s.split(" ")
        if len(pattern) != len(ls):
            return False
        dict_s = {}
        for index, value in enumerate(pattern):
            if dict_s.get(value, None):
                if dict_s[value] != ls[index]:
                    return False
            else:
                if ls[index] in dict_s.values():
                    return False
                dict_s[value] = ls[index]
        return True


s = Solution()
data = s.wordPattern(pattern = "abba", s = "dog dog dog dog")
print(data)
