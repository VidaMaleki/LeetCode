class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        
        for par in s:
            if par in matching: # if c is an opening bracket
                stack.append(par)
            else:
                if not stack:
                    return False
                
                pair = stack.pop()
                if matching[pair] != par:
                    return False
 
        return not stack