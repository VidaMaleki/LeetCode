class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in ransomNote:
            dict1[i] = dict1.get(i, 0) + 1
            
        for j in magazine:
            dict2[j] = dict2.get(j, 0) + 1
            
        for k, v in dict1.items():
            if k not in dict2 or dict1[k] > dict2[k]:
                return False
        return True