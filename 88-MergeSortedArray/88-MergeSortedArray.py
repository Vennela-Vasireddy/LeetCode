# Last updated: 11/15/2025, 6:24:54 PM
# def move(index, element, nums1):
#         for x in range(index+1, len(nums1)-1):
#             nums1[x] = nums1[x+1]
#         nums1[index] = element
#         return nums1
class Solution:
    
            
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range (n):
            nums1[m+x] = nums2[x]
        return nums1.sort()
            
        
#         for x in range(0, len(nums1)-len(nums2)):
#             for y in range(0, len(nums2)):
#                 if(nums1[x] >= nums2[y]):
#                     nums1 = move(x, nums2[x], nums1)
#                     break
#         return nums1
                
    
            
                
            
            
            