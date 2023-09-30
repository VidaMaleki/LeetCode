class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        q = int(s)+1
        q = list(str(q))
        q = [int(i) for i in q]
        return q

        

    