class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for par in s:
            if par in {"(", "[", "{"}:
                stack.append(par)
            elif par in pairs:
                if not stack or stack[-1] != pairs[par]:
                    return False
                stack.pop()
        return not stack

        