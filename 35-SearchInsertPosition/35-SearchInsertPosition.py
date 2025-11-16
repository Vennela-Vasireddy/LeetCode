# Last updated: 11/15/2025, 6:25:02 PM
def binarySearch(self, nums, initial, end, target):
    if end>=initial:
        mid = initial + (end - initial)//2
        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            return binarySearch(self,nums,initial ,mid-1, target)
            
        else:
            return binarySearch(self,nums, mid+1, end, target)
    else:
        return initial
        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        intial = 0 
        end = len(nums)-1
        value = binarySearch(self,nums, intial, end, target)
        return value

    
            
            
        
        
        
        