from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for char_s , char_t in zip(s, t):

            if s_map.get(char_s,char_t ) != char_t or t_map.get(char_t,char_s ) != char_s:
                return False
            s_map[char_s] = char_t
            t_map[char_t] = char_s
            
        return True
