class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagarams = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in anagarams:
                anagarams[temp].append(word)
            else:
                anagarams[temp] = [word]
        return [v for v in anagarams.values()]
