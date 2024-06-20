class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=nums[0]
        for x in range(1,len(nums)):
            k=k^nums[x]
        return k
        