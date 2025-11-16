# Last updated: 11/15/2025, 6:24:52 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
       
        for x in range(0, len(prices)-1):
            if(prices[x+1]>prices[x]):
                profit = profit + (prices[x+1] - prices[x])
                
        return profit
                
                
           
            
     

            
        
            
            
            
            
            
        
       
    
        