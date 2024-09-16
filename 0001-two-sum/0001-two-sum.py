class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for x in range(len(nums)):
        #     indices = []
        #     for y in range(x+1, len(nums)):
        #         if(target - nums[x] == nums[y]):
        #             indices.append(x)
        #             indices.append(y)
        #             return indices
                        
        indices = []
        for x in range(0, len(nums)):
            if ((target - nums[x]) in nums[x+1:len(nums)]):
                indices.append(x)
                indices.append(nums.index(target - nums[x], x+1, len(nums)))
                return indices
                
                
                
                        
                    
                    
        
                
                
        