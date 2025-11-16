# Last updated: 11/15/2025, 6:24:59 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return(len(s.split()[len(s.split())-1]))