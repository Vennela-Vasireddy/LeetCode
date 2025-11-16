# Last updated: 11/15/2025, 6:25:09 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = sorted(strs, key = len)
        result=[]
        string = ""
        if(len(new) == 1):
            return new[0]
        for x in range(0, len(new[0])):
            for y in range(0, len(new)):
                result.append(new[y][x])
            if(len(set(result))==1):
                string = string+result[0]
                result = [] 
        return string



        