import math
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        j = x
        mid = -1
        if x == 0 or x==1:
            return x
        while(i<j-1):
            mid = math.floor((i + j)/2)
            if(mid*mid > x):
                j = mid
            elif( mid*mid == x ):
                return int(mid)
            else:
                i = mid
        return i

    
            
        
        