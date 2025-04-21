class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp not in sorted_dict:
                sorted_dict[temp] = [word]
            else:
                sorted_dict[temp].append(word)
        return list(sorted_dict.values())