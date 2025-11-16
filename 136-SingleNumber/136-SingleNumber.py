# Last updated: 11/15/2025, 6:24:51 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=nums[0]
        for x in range(1,len(nums)):
            k=k^nums[x]
        return k
        