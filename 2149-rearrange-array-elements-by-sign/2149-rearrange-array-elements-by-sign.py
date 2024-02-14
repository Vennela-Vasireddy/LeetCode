class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        for x in nums:
            if x>0:
                positive.append(x)
            else:
                negative.append(x)
        for x in range(int(len(nums)/2)):
            result.append(positive[x])
            result.append(negative[x])
        return result
            
            
        