class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # min_price = prices[0]
        # max_profit = 0

        # for price in prices:

        #     min_price = min(min_price, price)

        #     profit = price - min_price

        #     max_profit = max(max_profit, profit)

        # return max_profit
    
    ##or

        i=0
        j=1
        max_profit=0
        while j<len(prices):
            if prices[j]-prices[i] > max_profit:
                max_profit=prices[j]-prices[i]
            
            if prices[i] > prices[j]:
                i=j
            j+=1
        return max_profit
