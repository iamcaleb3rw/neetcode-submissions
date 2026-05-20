class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < l:
                l = prices[i]
            elif prices[i] - l > maxProfit:
                maxProfit = prices[i] -l

        return maxProfit    

