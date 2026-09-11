class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = {}
        for char in s:
            anagram[char] = anagram.get(char, 0) +1
        
        for char in t:
            if char not in anagram or anagram[char]<= 0:
                return False
            anagram[char] -= 1
        return True