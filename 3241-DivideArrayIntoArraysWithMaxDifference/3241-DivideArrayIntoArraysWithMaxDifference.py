# Last updated: 11/15/2025, 6:24:22 PM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_nums =  sorted(nums)
        diff_nums = []
        count_diff = 0
        for x in range(0, len(sorted_nums), 3):
            diff_nums.append(sorted_nums[x:x+3])
        # print(range(0, int(len(nums)/3)))
        for x in range(0, int(len(nums)/3)):
            if( (diff_nums[x][2] - diff_nums[x][1]) <= k and 
                (diff_nums[x][1] - diff_nums[x][0]) <= k and
                (diff_nums[x][2] - diff_nums[x][0]) <= k ):
                
                count_diff +=1
                
             #   print(diff_nums[x][2] - diff_nums[x][1],
             #   diff_nums[x][1] - diff_nums[x][0],
             #  diff_nums[x][2] - diff_nums[x][0])
        if (count_diff == int(len(nums)/3)):
            return diff_nums
        return []
                    
                
                
                
            
        
        
        
        