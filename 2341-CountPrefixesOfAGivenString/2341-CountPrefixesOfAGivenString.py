# Last updated: 11/15/2025, 6:24:25 PM
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        l=[]
        for x in range(len(s)):
            l.append(s[0:x+1])
        for x in words:
            if x in l:
                c=c+1
                
        return c

        