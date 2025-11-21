class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left= 0
        longest = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in longest:
                longest.remove(s[left])
                left+=1
            longest.add(s[i])
            max_len = max(max_len, len(longest))
            
        return max_len
 