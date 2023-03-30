class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        c = path.split("/")
        
        for char in c:
            if char == "..":
                if stack:
                    stack.pop()
            elif char == "." or char == "":
                continue
            else:
                stack.append(char)
            print(stack)
        return "/" + "/".join(stack)