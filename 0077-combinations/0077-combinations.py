from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        possible = list(range(1,n+1))
        output = []
        comb = combinations(possible, k)
        for x in comb:
            output.append(list(x))
        return output
        