# Last updated: 11/15/2025, 6:25:00 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0 
        max_sum = -100000
        for x in nums:
            current_sum +=x
            if(current_sum > max_sum):
                max_sum = current_sum
            if(current_sum < 0):
                current_sum = 0
        return max_sum
#         max_sum = -100000
#         sub_list_sum = 0
#         result = []
#         i,j = 0,0
#         while(i!=len(nums) and j!=len(nums)):
#             sub_list_sum = sub_list_sum + nums[j]
#             if(sub_list_sum > max_sum):
#                 max_sum = sub_list_sum
#                 result = nums[i:j+1]
#             j=j+1
#             if(j==len(nums)):
#                 i=i+1
#                 j=i
#                 sub_list_sum = 0
#         return sum(result)
#  Above is brute force

    
    
            
            
            
            
            
            
            
            
        