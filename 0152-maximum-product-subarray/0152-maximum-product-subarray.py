class Solution:
    def maxProduct(self, nums: List[int]) -> int:
 #       Brute force
        max_product = -100000
        for x in range(len(nums)):
            current_product = 1
            for y in nums[x:len(nums)]:
                current_product *=y
                if(max_product < current_product ):
                    max_product = current_product
        return max_product
                
                
#         max_product = -100000
#         current_product = 1
#         count = 0
#         last_negative_element = 0
#         if(len(nums)==1): return nums[0]
#         if(nums[0]==0):
#             nums[0]=1
            
#         for x in range(len(nums)):
#             if(nums[x]<0): 
#                 count = count +1
#                 last_negative_element = x
        
#         if(count % 2 ==0 ):
#             max_product = nums[0]
#             for x in range(len(nums)):
#                 current_product = current_product*nums[x]
#                 if(current_product >=0 and max_product <= current_product):
#                     max_product =  current_product 
                
#         else:
#             if(count >1):
#                 nums[last_negative_element] = 0
#             max_product = nums[0]
#             for x in range(len(nums)):
#                 current_product = current_product*nums[x]
#                 if(current_product >=0  and max_product <= current_product):
#                     max_product =  current_product
#                 if(current_product == 0 and max_product>=0 ):
#                     current_product = 1
                
            
#         return max_product
                
            
            
        
            
            
        