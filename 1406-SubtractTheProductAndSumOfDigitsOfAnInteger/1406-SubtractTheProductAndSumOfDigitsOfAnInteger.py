# Last updated: 11/15/2025, 6:24:39 PM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        m=1
        a=0
        for x in s:
            m=m*int(x)
            a=a+int(x)
        
        return m - a

        
        