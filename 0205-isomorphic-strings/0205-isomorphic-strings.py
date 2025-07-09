class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for s_char, t_char in zip(s, t):
            if s_dict.get(s_char, t_char) != t_char or t_dict.get(t_char, s_char) != s_char:
                return False
            s_dict[s_char] = t_char
            t_dict[t_char] = s_char
            
        return True
            
