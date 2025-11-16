# Last updated: 11/15/2025, 6:24:36 PM
class Solution:
    def average(self, salary: List[int]) -> float:
        s = sorted(salary)
        return( sum(s[1:len(salary)-1])/int(len(salary)-2) )
        