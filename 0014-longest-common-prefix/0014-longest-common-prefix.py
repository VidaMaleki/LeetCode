class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        ans = ""
        
        for i in range(len(first)): # f l o w 
            j = 0
            while first[i]:
                if first[i] != sorted_strs[j][i]:
                    return ans
                j+=1
                if j > len(sorted_strs) -1:
                    break
            ans += first[i]
            
        return ans