class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            indices = []
            for y in range(x+1, len(nums)):
                if(target - nums[x] == nums[y]):
                    indices.append(x)
                    indices.append(y)
                    return indices
                        
                        
                    
                    
        
                
                
        