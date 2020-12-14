class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashTable = {}
        for word in strs:
            temp = sorted(word)
            tempStr = "".join(temp)
            if tempStr not in hashTable:
                hashTable[tempStr] = []
            hashTable[tempStr].append(word)
        return hashTable.values()



s = Solution()
data = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(data)