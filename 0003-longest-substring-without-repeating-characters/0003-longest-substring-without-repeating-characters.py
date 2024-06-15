class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in s[left:i]:
                print("if", s[i], " ans: ", ans)
                ans = max(ans, len(s[left:i+1]))
            else:
                while s[i] in s[left:i]:
                    print("else", s[i])
                    left +=1
            
        return ans