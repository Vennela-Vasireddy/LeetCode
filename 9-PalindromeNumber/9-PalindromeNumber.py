# Last updated: 11/15/2025, 6:25:12 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if(s==s[::-1]):
            return 1
        else:
            return 0
        