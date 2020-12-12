class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if len(bills) == 0:
            return True
        if bills[0] != 5:
            return False
        charges = [bills.pop(0)]
        for i in bills:
            if i == 5:
                charges.append(5)
            elif i == 10:
                if 5 in charges:
                    charges.remove(5)
                    charges.append(10)
                else:
                    return False
            else:
                if 10 in charges and 5 in charges:
                    charges.remove(5)
                    charges.remove(10)
                elif charges.count(5) >= 3:
                    for i in range(3):
                        charges.remove(5)
                else:
                    return False
        return True


s = Solution()
data = s.lemonadeChange([5,5,10, 20])
print(data)

