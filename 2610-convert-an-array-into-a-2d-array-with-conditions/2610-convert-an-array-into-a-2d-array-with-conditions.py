class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        array_2d = []
        if(len(nums)==len(set(nums))):
            array_2d.append(nums)
        else:
            while len(nums)!=0:
                array_2d.append(list(set(nums)))
                for x in set(nums):
                    nums.remove(x)
        return array_2d
            
            
            
        