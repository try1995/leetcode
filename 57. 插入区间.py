class Solution:
    def insert(self, intervals, newInterval):
        left, right = newInterval
        placed = False
        ans = []
        for li, ri in intervals:
            if li > right:
                if not placed:
                    ans.append(left, right)
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans


s = Solution()
data = s.insert(intervals = [], newInterval = [4,8])
print(data)
