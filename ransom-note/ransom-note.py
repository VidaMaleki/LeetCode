class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {i: ransomNote.count(i) for i in set(ransomNote)}
        dict2 = {i: magazine.count(i) for i in set(magazine)}
            
        for k, v in dict1.items():
            if k not in dict2 or dict1[k] > dict2[k]:
                return False
        return True