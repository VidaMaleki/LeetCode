from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_map = Counter(ransomNote)
        magazine_map = Counter(magazine)
        for k, v in ransome_map.items():
            if k not in magazine_map or v > magazine_map[k]:
                return False
        return True
