class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even_index, odd_index = 0,1
        result = [0]*len(nums)
        for x in nums:
            if x>0:
                result[even_index] = x
                even_index +=2
            else:
                result[odd_index] = x
                odd_index +=2
        return result
                
        
        
            
        