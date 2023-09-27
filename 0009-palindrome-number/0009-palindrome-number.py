class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = str(x)
        left = 0
        right = len(x_copy)-1
        while left < right:
            if x_copy[left] != x_copy[right]:
                return False
            left +=1
            right -= 1
        return True
        