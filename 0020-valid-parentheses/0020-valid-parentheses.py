class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        for par in s:
            if par in matching:
                stack.append(par)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if par != matching[pair]:
                    return False
        return len(stack) == 0