class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            remainder = x%3
            if remainder !=0:
                count = count + 1
        return count
            