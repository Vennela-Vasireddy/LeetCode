# Last updated: 11/15/2025, 6:24:45 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        word_list = s.split(" ")
        if(len(pattern)!=len(word_list)):
            return False
        for x in range(len(pattern)):
            if pattern[x] in word_dict:
                if((word_dict[pattern[x]] != word_list[x])):
                    return False
            
            word_dict[pattern[x]] = word_list[x]
        if(len(list(set(list(word_dict.keys())))) != len(list(set(list(word_dict.values()))))):
            return False
            
        return True
                
                
  
            
        