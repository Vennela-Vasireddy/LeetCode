class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        arr.append(pref[0])
        for x in range(0, len(pref)-1):
            arr.append(pref[x+1]^pref[x])
        return arr
            
            
            
        
        