class Solution:
    def isValid(self, s: str) -> bool:
#         dictionary = { ')':'(' ,'}':'{', ']' : '[' }
#         stack = []
#         for x in range(0,len(s)):
#             if s[x] in ['(','{', '[']:
#                 stack.append(s[x])
#             else:
#                 if len(stack) == 0 : return False

#                 if stack.pop()!= dictionary[s[x]]:
#                     return False
#             return True
        
        stack = []
        mapping = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if not stack: return False
                if stack.pop() != mapping[i]:
                    return False
        return not stack