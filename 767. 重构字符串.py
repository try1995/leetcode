from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = [""] * len(S)
        tmp = []
        count = Counter(S)
        count = sorted(count.items(), key=lambda x: x[1])
        if count[-1][1] > (len(S) + 1) // 2:
            return ""
        for key, value in count:
            tmp.extend(key * value)

        # 单号和双号
        # 单号排temp左半边的元素，双号排temp右半边的元素
        res[::2], res[1::2] = tmp[len(S) // 2:], tmp[:len(S) // 2]

        return ''.join(res)


s = Solution()
data = s.reorganizeString("aab")
print(data)
