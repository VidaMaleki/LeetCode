class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            temp = tuple(sorted(word))
            anagram_map.setdefault(temp, []).append(word)
        return list(anagram_map.values())
