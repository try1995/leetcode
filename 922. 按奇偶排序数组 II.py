class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        def swap(a, b):
            temp = A[a]
            A[a] = A[b]
            A[b] = temp

        dict_A = {0: [], 1: []}
        for index, value in enumerate(A):
            flag = index % 2
            if flag != value % 2:
                dict_A[flag].append(index)
        for i, j in enumerate(dict_A[0]):
            swap(j, dict_A[1][i])
        return A


s = Solution()
data = s.sortArrayByParityII([4, 2, 5, 7])
print(data)
