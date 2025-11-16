# Last updated: 11/15/2025, 6:25:05 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j=j+1
                
        return j
                
        
        