class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for x in s:
            count[x] = count.get(x,0)+1
        if len(set(count.values())) == 1:
            return True
        return False