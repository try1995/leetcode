from collections import Counter


class Solution:
    def commonChars(self, A):
        res = []
        for c in set(A[0]):
            count = [w.count(c) for w in A]
            s = c * min(count)  # 如果不是每个单词都有的字母，min(count)=0
            # for a in s:
            res += s
        return res

s = ["bella","label","roller"]
so = Solution()
data = so.commonChars(s)
print(data)
