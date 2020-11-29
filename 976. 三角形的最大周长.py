class Solution(object):
    # 边已经排好序了，只需要判断两个小边相加大于大边
    def check(self, a, b, c):
        return b+c > a

    def largestPerimeter(self, A:list):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            a = A[i]
            b = A[i + 1]
            c = A[i + 2]
            if self.check(a, b, c):
                return a + b + c
        return 0


s = Solution()
data = s.largestPerimeter([3,6,2,3])
print(data)