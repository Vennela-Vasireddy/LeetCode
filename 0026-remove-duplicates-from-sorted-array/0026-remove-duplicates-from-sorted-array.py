class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while(i!=len(nums) and j!=len(nums) ):
            if(nums[i] != nums[j]):
                nums[i+1],nums[j] = nums[j],nums[i+1]
                i = i+1
            j=j+1
        return len(set(nums))