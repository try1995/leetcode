class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = []
        dire = []
        for index, value in enumerate(senate):
            if value == "R":
                radiant.append(index)
            else:
                dire.append(index)
        while True:
            if len(radiant) == 0:
                return "Dire"
            if len(dire) == 0:
                return "Radiant"
            r = radiant.pop(0)
            d = dire.pop(0)
            if r < d:
                radiant.append(r+len(senate))
            else:
                dire.append(d+len(senate))


s = Solution()
data = s.predictPartyVictory("DDRRR")
print(data)
