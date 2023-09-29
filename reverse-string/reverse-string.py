class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)
    
        while left < right:
            print("left: ", left, "right: ", right)
            temp = s.pop()
            s.insert(left, temp)
            left +=1

        return s
        