from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = Counter(S)
        count = sorted(count.items(), key=lambda x: x[1])
        if len(count) < 2:
            return ""
        flag = count[0][1]
        ret = [count[0][0]] * count[0][1]
        count.pop(0)
        for value, nums in count:
            if nums <= flag + 1:
                flag = flag + nums + 1
                for i in range(nums):
                    ret.insert(2*i, value)
            else:
                return ""
        return "".join(ret)


s = Solution()
data = s.reorganizeString("apyvzaaaabaaruraaaadwabldaralasahaaamrsaaaaaaaxaauwaaaafavaaabqieqkauyxgawdiabajakxmaaaawhabzaabaiahaaaarxmvamaanalaadahwbaadtarazjjavbswkaaaaacoaaakaazaramftialshqaaamlvhaankeaaaaaavayzadaaasathjaaanyaakrhueaiamaafapvaaaaeauaacyaaaroawaoaaadaagaaugkaaaamabbduaaacaaxaataauuaeaoaiqtlaaqqtarlaaaaajcaaaajgcgaodaadaoqasaaaalesaaapaascacavwdnnasxaayatawvikazaaadajatasanaaaamapuaavtaaseadzvaxaaaaapoaapsaaakraaakaiafataaaaaaaxljmgaaaavhaaalaeaaaazayazqaekqykzaaabsybvdxxvbaaaaajvaaidntlaagaaajzaleataek")
print(data)
