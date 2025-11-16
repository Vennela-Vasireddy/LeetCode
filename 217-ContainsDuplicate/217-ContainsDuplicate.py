# Last updated: 11/15/2025, 6:24:47 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for x in range(0, len(nums)-1):
            if(nums[x]^nums[x+1] == 0):
                return True
        return False