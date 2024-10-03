from itertools import permutations 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        string = ''
        result = []
        sequence = [x for x in range(1, n+1)]
        perm = permutations(sequence)
        for x in perm:
            count = count+1
            if(count == k):
                result = x
                break
        return ''.join(map(str, result))
        