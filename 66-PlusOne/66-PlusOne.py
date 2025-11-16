# Last updated: 11/15/2025, 6:24:58 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        s=''
        for x in range(0,len(digits)):
            s=s+str(digits[x])
        a=int(s)+1
        for x in str(a):
            l.append(int(x))
            
        return l
                
