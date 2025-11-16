# Last updated: 11/15/2025, 6:24:42 PM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)-1,1,-1):
            if (nums[x-1]+nums[x-2]>nums[x]):
                return (nums[x-1]+nums[x-2]+nums[x])
        return 0