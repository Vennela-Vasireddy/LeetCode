# Last updated: 11/15/2025, 6:25:10 PM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        i = 0
        l=[]
        for x in s:
            l.append(d[x])
        for x in range(0, len(l)-1):
            if len(l) == 1:
                return l[x]
            else:
                if(l[x]<l[x+1]):
                    l[x] = l[x]*(-1)
        return sum(l)
                    
        