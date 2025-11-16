# Last updated: 11/15/2025, 6:24:34 PM
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for x in range(0,len(arr)):
            for y in range(x+1,len(arr)+1):
                if(len(arr[x:y])%2!=0):
                    s=s+sum(arr[x:y])
        return s
                    
                
        