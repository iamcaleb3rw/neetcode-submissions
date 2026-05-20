class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if i < j:
                    newProfit = prices[j] - prices[i]
                    maxProfit = max(maxProfit, newProfit)
        return maxProfit            