# Last updated: 11/15/2025, 6:25:03 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                else:
                    j -= 1
            else:
                i += 1
        return i 
            

            
            
            
                
                
            
        
        
        
        