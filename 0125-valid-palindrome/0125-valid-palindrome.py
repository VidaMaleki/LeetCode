class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for i in s:
            if i.isalnum() :
                s2 += i
        print(s2)
        return s2.lower() == s2[::-1].lower()
        