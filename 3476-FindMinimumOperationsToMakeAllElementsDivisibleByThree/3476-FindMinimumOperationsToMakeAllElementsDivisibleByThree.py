# Last updated: 11/15/2025, 6:24:21 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if x%3 !=0:
                count = count + 1
        return count
            