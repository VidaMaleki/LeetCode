class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        answer= ""
        
        i = 0
        if s[0] in "+-":
            sign = -1 if s[0] == "-" else 1
            i = 1

        while i < len(s) and s[i].isdigit():
            answer += s[i]
            i+=1

        if not answer:
            return 0
        val = int(answer) * sign

        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if val < INT_MIN: return INT_MIN
        if val > INT_MAX: return INT_MAX
        return val