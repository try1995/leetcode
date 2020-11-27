class Solution:
    def kClosest(self, points, K: int):
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[0:K]


s = Solution()
data = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
print(data)
