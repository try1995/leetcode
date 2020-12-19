class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ls = [[] for _ in range(len(matrix))]
        for value in matrix[::-1]:
            for i in range(len(matrix)):
                ls[i].append(value[i])
        for i in range(len(matrix)):
            matrix[i] = ls[i]


s = Solution()
s.rotate(matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], )