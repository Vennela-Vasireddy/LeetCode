# Last updated: 11/15/2025, 6:24:44 PM
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        for x in s:
            if(x in t):
                t=t.replace(x,"",1)
        return t
        