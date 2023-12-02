class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left = 0
        right = len(s) -1
        while left <= right:
            print(s[left], s[right])
            if not s[left].isalnum():
                left +=1
            if not s[right].isalnum():
                right -=1
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left +=1
                    right -=1
                else:
                    return False
        return True
        
                