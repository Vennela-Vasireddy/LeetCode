# Last updated: 11/15/2025, 6:25:13 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0
        maxLength = 0
        while(r < len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxLength = max(maxLength, r - l+1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l = l+1
                charSet.add(s[r])
            r = r+1
        return maxLength
            
            
            

        