# Last updated: 11/15/2025, 6:24:41 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x*x for x in nums]
        # for x in range(0, len(nums)):
        #     for y in range(0, x):
        #         if(nums[x]<nums[y]):
        #             nums[x], nums[y] = nums[y], nums[x]
        return sorted(nums)
        
        