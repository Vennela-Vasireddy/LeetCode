class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Traverse through each sentence and find out the words by checking whether the literal == " " and increase count and return the max count - This is a bruteforce approach
        
        max_count = 0
        for sentence in sentences:
            current_count = 0
            for literal in sentence:
                if literal == " ":
                    current_count = current_count + 1
            max_count = max(current_count, max_count)
        return max_count+1
                
            
            
            
        
        