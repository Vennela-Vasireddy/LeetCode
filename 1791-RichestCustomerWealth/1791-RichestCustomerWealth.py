# Last updated: 11/15/2025, 6:24:33 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max( sum(i)  for i in accounts )
            
        