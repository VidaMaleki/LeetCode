class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orginal_x = x
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return reversed_x == orginal_x