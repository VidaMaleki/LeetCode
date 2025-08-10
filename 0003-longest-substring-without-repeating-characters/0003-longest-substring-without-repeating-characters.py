class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        max_sub = 0
        left = 0
        for right, char in enumerate(s):
            while char in sub_string:
                sub_string.remove(s[left])
                left +=1
            sub_string.add(char)
            max_sub = max(max_sub, right-left +1)
        return max_sub