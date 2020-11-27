class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # TODO sort
        count = 0
        for i in A:
            for j in B:
                for k in C:
                    for m in D:
                        if i + j + k + m == 0:
                            count += 1
        return count


s = Solution()
data = s.fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2])
print(data)
