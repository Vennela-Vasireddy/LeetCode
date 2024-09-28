class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while(r < len(prices)):
            if(prices[l] > prices[r]):
                l = r
            else:
                profit = prices[r] - prices[l]
                print(profit)
                max_profit = max(max_profit, profit)
            r = r+1
        return max_profit
                
            
            
            
        
        
        
        