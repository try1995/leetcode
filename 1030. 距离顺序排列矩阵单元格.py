class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        points = []
        for x in range(R):
            for y in range(C):
                points.append([x, y])
        points = sorted(points, key=lambda x: pow(x[0] - r0, 2) + pow(x[1] - c0, 2))
        return points


s = Solution()
data = s.allCellsDistOrder(R = 2, C = 3, r0 = 1, c0 = 2)
print(data)
