class Solution:
    def maxProfit(self, prices) -> int:
        len_prices = len(prices)
        if len_prices < 2:
            return 0
        pre = 1
        sum_profit = 0
        while pre < len_prices:
            if prices[pre] > prices[pre - 1]:
                sum_profit += prices[pre] - prices[pre-1]
            pre += 1
        return sum_profit


s = Solution()
data = s.maxProfit([6,1,3,2,4,7])
print(data)
