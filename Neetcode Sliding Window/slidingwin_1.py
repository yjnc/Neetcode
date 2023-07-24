class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maxprofit = 0
        # Initialize min to biggest number to be replaced as we iterate
        min_price = float('inf')
        
        for price in prices:
            maxprofit = max(maxprofit, price - min_price)
            min_price = min(min_price, price)

        return maxprofit


solution = Solution()
prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices))