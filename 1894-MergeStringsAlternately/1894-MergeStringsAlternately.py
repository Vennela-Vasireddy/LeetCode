# Last updated: 11/15/2025, 6:24:29 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s1=""
        if(len(word1)==len(word2)):
            for x in range(len(word1)):
                s1=s1+word1[x]+word2[x]
            return s1
        l=len(word1)-len(word2)
        if(l>0):
            for x in range(len(word2)):
                s1=s1+word1[x]+word2[x]
            return s1+word1[len(word2):len(word1)]
        else:
            for x in range(len(word1)):
                s1=s1+word1[x]+word2[x]
            return s1+word2[len(word1):len(word2)]
            
        
           
            
            
                
            
        
            
        