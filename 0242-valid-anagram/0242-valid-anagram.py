class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted(list(s)))
        print(sorted(list(t)))
        return sorted(list(s)) == sorted(list(t))