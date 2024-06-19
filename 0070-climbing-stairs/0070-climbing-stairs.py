class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,1,2]
        for x in range(3, n+1):
            fib.append(fib[x-1]+fib[x-2])
        return fib[n]
            
    
            
        