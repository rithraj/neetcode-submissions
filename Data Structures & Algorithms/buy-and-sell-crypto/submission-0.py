class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')

        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            currProfit = prices[i] - buy
            if currProfit > profit:
                profit = currProfit
        
        return profit

        