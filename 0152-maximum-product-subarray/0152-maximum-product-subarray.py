class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -100000
        for x in range(len(nums)):
            current_product = 1
            for y in nums[x:len(nums)]:
                current_product *=y
                if(max_product < current_product ):
                    max_product = current_product
        return max_product
                
                
#         max_product = 0
#         current_product = 1
#         sign = []
#         if(len(nums)==1): return nums[0]
#         for x in nums:
#             sign.append(1 if x >= 0 else 0)
        
#         if( (sign.count(0))%2 ==0 ):
#             for x in range(len(nums)):
#                 if(nums[x]==0): nums[x] = 1 
#                 current_product = current_product*nums[x]
#                 if(max_product <= current_product):
#                     max_product =  current_product 
#         else:
#             for x in range(len(nums)):
#                 current_product = current_product*nums[x]
#                 if(current_product >=0  and max_product <= current_product):
#                     max_product =  current_product
                
            
#         return max_product
                
            
            
        
            
            
        