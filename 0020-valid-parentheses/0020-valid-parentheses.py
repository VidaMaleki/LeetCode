class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in par:
                if not stack or stack[-1] != par[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
        