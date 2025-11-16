# Last updated: 11/15/2025, 6:25:07 PM
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if not stack: return False
                if stack.pop() != dictionary[i]:
                    return False
        return len(stack)==0
        
        
        # stack = []
        # mapping = {
        #     ")": "(", 
        #     "]": "[", 
        #     "}": "{"
        # }
        # for i in s:
        #     if i in ["(", "[", "{"]:
        #         stack.append(i)
        #     else:
        #         if not stack: return False
        #         if stack.pop() != mapping[i]:
        #             return False
        # return not stack