# Last updated: 11/15/2025, 6:24:35 PM
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        for x in range(0,len(mat)):
            if(x != len(mat)-1-x):
                s=s+mat[x][x]
            s=s+mat[x][len(mat)-1-x]
                        

        return s
            
            