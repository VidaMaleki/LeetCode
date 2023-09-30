class Solution:
    def countElements(self, arr: List[int]) -> int:
        s_set = set(arr)
        counter = 0
        for i in arr:
            print (i , s_set)
            if i+1 in s_set:
                counter += 1
        return counter