class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp not in strs_dict:
                strs_dict[temp] = [word]
            else:
                strs_dict[temp].append(word)
                
        return strs_dict.values()
            