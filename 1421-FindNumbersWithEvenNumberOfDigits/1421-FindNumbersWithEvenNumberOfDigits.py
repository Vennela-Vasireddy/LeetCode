# Last updated: 11/15/2025, 6:24:38 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            count = math.floor(math.log10(num))+1
            # while(num>0):
            #     num = num//10
            #     count = count + 1
            if(count%2 == 0):
                even_count = even_count + 1
        return even_count
                
        
        