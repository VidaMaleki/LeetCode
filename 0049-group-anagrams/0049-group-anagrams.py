class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in strs_dict:
                strs_dict[temp].append(word)
            else:
                strs_dict[temp] = [word]
                
        return strs_dict.values()
            