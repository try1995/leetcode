class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        query = []
        len_all = len(nums1) + len(nums2)
        while True:
            if len(nums1) == 0:
                query.extend(nums2)
                break
            if len(nums2) == 0:
                query.extend(nums1)
                break
            if nums1[0] < nums2[0]:
                query.append(nums1.pop(0))
            else:
                query.append(nums2.pop(0))
            if len(query) > len_all / 2:
                if len_all % 2 == 0:
                    return (query[len_all // 2 -1] + query[len_all // 2]) / 2
                else:
                    return query[int(len_all / 2)]
        if len_all % 2 == 0:
            return (query[len_all // 2 - 1] + query[len_all // 2]) / 2
        else:
            return query[int(len_all / 2)]


s = Solution()
data = s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,7])
print(data)
