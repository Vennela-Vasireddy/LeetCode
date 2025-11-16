# Last updated: 11/15/2025, 6:24:41 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

    	S = []
    	for i in arr2:
    		j = 0
    		while j < len(arr1):
    			if arr1[j] == i:
    				S += [i]
    				del arr1[j]
    				j -= 1
    			j += 1
    	return(S+sorted(arr1))
            
            
            
                    
                    

                
                
        
        