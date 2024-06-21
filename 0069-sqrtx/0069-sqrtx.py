import math
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        j = x
        mid = -1
        if x == 0 or x==1:
            return x
        while(i<j-1):
            mid = math.floor(i + 0.5 * (j - i))
            if(mid*mid > x):
                j = mid
            elif( mid*mid == x ):
                return int(mid)
            else:
                i = mid
        return i
                
            # import math

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         start = 1
#         end = x
#         mid = -1

#         if x == 0:
#             return 0

#         while start < end - 1:
#             mid = math.floor(start + 0.5 * (end - start))
#             mid_sq = mid * mid

#             if mid_sq > x:
#                 end = mid
#             elif mid_sq == x:
#                 return mid  # for perfect squares
#             else:
#                 start = mid

#         return start

    
            
        
        