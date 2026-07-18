class Solution:
    def reverseWords(self, s: str) -> str:
        splited_s = s.split()
        splited_s.reverse()
        return " ".join(splited_s)