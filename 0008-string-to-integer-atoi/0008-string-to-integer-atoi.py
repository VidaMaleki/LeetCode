class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[i] in ["+", "-"]:
            if s[i] == "-":
                sign = -1
            i +=1
        answer = 0
        while i < len(s) and s[i].isdigit():
            answer  = answer * 10 + int(s[i])
            i+=1
        
        answer *= sign
        MAX_NUM, MIN_NUM = 2**31-1, -2**31 
        if answer > MAX_NUM:
            return MAX_NUM
        if answer < MIN_NUM:
            return MIN_NUM
        return answer
