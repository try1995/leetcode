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
        queue = []
        while count:
            queue.append(count[0][0])
            queue.append(count[1][0])
            for i in range(len(count)-1):
                if count[i][1] < count[i+1][1]:
                    temp = count[i]
                    count[i] = count[i+1]
                    count[i+1] = temp
                else:
                    break
        return "".join(queue)


s = Solution()
data = s.reorganizeString("apyvzaaaabaaruraaaadwabldaralasahaaamrsaaaaaaaxaauwaaaafavaaabqieqkauyxgawdiabajakxmaaaawhabzaabaiahaaaarxmvamaanalaadahwbaadtarazjjavbswkaaaaacoaaakaazaramftialshqaaamlvhaankeaaaaaavayzadaaasathjaaanyaakrhueaiamaafapvaaaaeauaacyaaaroawaoaaadaagaaugkaaaamabbduaaacaaxaataauuaeaoaiqtlaaqqtarlaaaaajcaaaajgcgaodaadaoqasaaaalesaaapaascacavwdnnasxaayatawvikazaaadajatasanaaaamapuaavtaaseadzvaxaaaaapoaapsaaakraaakaiafataaaaaaaxljmgaaaavhaaalaeaaaazayazqaekqykzaaabsybvdxxvbaaaaajvaaidntlaagaaajzaleataek")
print(data)
