# Last updated: 11/15/2025, 6:24:48 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')
            
        