class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            if 0 not in nums:
                return 0
            if 1 not in nums:
                return 1
            if 2 not in nums:
                return 2
        else:
            if(max(nums)==len(nums)):
                return int(((max(nums)*(max(nums)+1))/2) - sum(nums))
            else:
                return len(nums)
        