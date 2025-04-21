class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        s_map = {}
        pattern_map = {}
        for char_s, char_p in zip(pattern, s_list):
            if s_map.get(char_s, char_p) != char_p or pattern_map.get(char_p, char_s) != char_s:
                return False
            s_map[char_s] = char_p
            pattern_map[char_p] = char_s
        return True