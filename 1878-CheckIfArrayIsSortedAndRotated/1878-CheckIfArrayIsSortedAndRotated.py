# Last updated: 11/15/2025, 6:24:30 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
# brute force
        sorted_nums = sorted(nums)
        for x in range(len(nums)):
            count = 0
            for i in range(len(nums)):
                if(sorted_nums[i] == nums[(i+x) % len(nums)]):
                    count = count+1
            if count == len(nums):
                return True 
        return False
                    
                
                
        
        
        