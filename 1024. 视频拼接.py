class Solution:
    # 剪枝，每次取差距最多的片段，贪心
    def max_diff(self, dict_a, vil, val):
        diff = -1
        max_key = 0
        for key, value in dict_a.items():
            if key > vil and key <= val and value > val:
                dif = value - val
                if dif > diff:
                    diff = dif
                    max_key = key
        return max_key

    def videoStitching(self, clips, T: int) -> int:
        dict_a = {}
        for i in clips:
            left = i[0]
            right = dict_a.get(left, -1)
            if right < i[1]:
                dict_a[left] = i[1]

        left = min(dict_a.keys())
        right = max(dict_a.values())
        if right < T or left > 0:
            return -1
        max_step = 101
        def helper(vil, val, step):
            nonlocal max_step
            if step > max_step:
                return
            if val >= T:
                max_step = step
                return
            max_key = self.max_diff(dict_a, vil, val)
            helper(max_key, dict_a[max_key], step + 1)
        helper(0, dict_a[0], 1)
        if max_step == 101:
            return -1
        else:
            return max_step


s = Solution()
data = s.videoStitching(clips=[[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]]
,T = 50)
print(data)
