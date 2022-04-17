class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_list=[]
        for candy in candies:
            if (candy + extraCandies) >= max(candies):
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list