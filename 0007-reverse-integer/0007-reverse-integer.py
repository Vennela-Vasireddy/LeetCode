class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        reverse_number = 0
        if(x<0):
            sign = True
            x = x*(-1)
            
        if x%10 == 0:
            x = x/10
            
        while(x>0):
            reverse_number = reverse_number*10 + int(x%10)
            x = int(x/10)
        reverse_number = reverse_number*(-1) if sign else reverse_number
        return 0 if( reverse_number > 2**31 -1 or reverse_number < -2**31  ) else reverse_number
    
            
        
        