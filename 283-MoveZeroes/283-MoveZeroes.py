# Last updated: 11/15/2025, 6:24:45 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=nums.count(0)
        for x in range(i):
            nums.remove(0)
            nums.append(0)
        return (nums)
        
    
            