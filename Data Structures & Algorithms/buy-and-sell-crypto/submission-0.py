class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        left = 0

        for right in range(1,len(prices)):
            diff = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(diff, profit)
            else:
                left = right
        return profit
        

