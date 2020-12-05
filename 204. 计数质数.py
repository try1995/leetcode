class Solution:
    def check(self, num):
        for i in range(2,int(pow(num,0.5))+1):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        count = 0
        for i in range(2, n):
            if self.check(i):
                count += 1
        return count


s = Solution()
data = s.countPrimes(10)
print(data)