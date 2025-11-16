# Last updated: 11/15/2025, 6:24:46 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(max(nums)==len(nums)):
            return int(((max(nums)*(max(nums)+1))/2) - sum(nums))
        else:
            return len(nums)
        