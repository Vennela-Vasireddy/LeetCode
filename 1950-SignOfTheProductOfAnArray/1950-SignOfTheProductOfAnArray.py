# Last updated: 11/15/2025, 6:24:28 PM
class Solution:
    
        
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for x in nums:
            product=product*x
        if(product>0):
            return 1
        elif(product==0):
            return 0
        else:
            return -1
        
    
        