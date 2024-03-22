class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(max(nums)==len(nums)):
            return int(((max(nums)*(max(nums)+1))/2) - sum(nums))
        else:
            return len(nums)
        