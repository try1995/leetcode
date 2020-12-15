class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        seed = 1
        while N:
            num = N % 10
            N = N // 10
            high = N % 10
            if high > num:
                res = seed*10 - 1
                N -= 1
            else:
                res = num*seed + res
            seed = seed * 10
        return res


s = Solution()
data = s.monotoneIncreasingDigits(332)
print(data)