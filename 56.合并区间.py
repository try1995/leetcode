class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:(x[0], x[1]))
        intervals.append([100000,100000])
        a = intervals.pop(0)
        ret = []
        while intervals:
            left, right = intervals.pop(0)
            # in
            if a == [left, right]:
                continue
            if left <= a[1]:
                if right > a[1]:
                    a[1] = right
            if left > a[1]:
                ret.append(a)
                a = [left, right]
        return ret


intervals = [[1,3],[2,6],[1,2] ,[8,10], [8,9],[15,18]]
app = Solution()
ret= app.merge(intervals)
print(ret)