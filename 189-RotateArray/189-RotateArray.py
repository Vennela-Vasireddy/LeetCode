# Last updated: 11/15/2025, 6:24:49 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k!=0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
    
        
        