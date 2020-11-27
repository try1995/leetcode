class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        res, t = 0, 0
        for i in range(len(gas)):
            t += gas[i] - cost[i]
            if t < 0:
                res = i + 1
                t = 0
        return res


s = Solution()
data = s.canCompleteCircuit(gas  = [1,2,3,4,5],cost = [3,4,5,1,2])
print(data)
