class Solution:
#     s = "()[]{}"
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in par:
                temp = stack.pop() if stack else "#"
                if par[char] != temp: 
                    return False
                
            else:
                stack.append(char)
        return not stack