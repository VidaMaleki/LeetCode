class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if len(x) <= 1:
            return True
        if x[0] != x[-1]:
            return False
        return self.isPalindrome(x[1:-1])