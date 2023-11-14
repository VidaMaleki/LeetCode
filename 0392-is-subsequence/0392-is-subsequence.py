class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        j = 0
        ans = ""
        while i != len(t):
            if s[j] == t[i]:
                j += 1
            i +=1
            if j == len(s):
                return True
        
        return False