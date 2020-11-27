from collections import Counter


class Solution(object):
    def relativeSortArray(self, arr1, arr2: list):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        con = Counter(arr1)
        ls_ex = []
        ls_be = []
        for i in arr1:
            if i not in arr2:
                ls_ex.append(i)
        ls_ex = sorted(ls_ex)
        for i in arr2:
            ls_be += [i] * con[i]
        return ls_be + ls_ex


s = Solution()
data = s.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6])
print(data)