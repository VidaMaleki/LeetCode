class Solution:
    def checkString(self, s: str) -> bool:
        s_dict = {}
        for x in s:
            s_dict[x] = s_dict.get(x, 0) +1
        #check if a exist and s start with a
        if "a" in s:
            len_a = s_dict['a']
            if s[:len_a] == ('a' * len_a):
                return True
        # if a not exist and if s not empty
        elif "a" not in s and s != '':
            return True 
        return False
            