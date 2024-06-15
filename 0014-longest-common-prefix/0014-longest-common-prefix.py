class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(strs, key=len)
        commons = []
        print(min_len)
        for i in range(len(min_len)):
            for word in strs:
                if min_len[i] != word[i]:
                    return min_len[:i]
        return min_len   
        
                