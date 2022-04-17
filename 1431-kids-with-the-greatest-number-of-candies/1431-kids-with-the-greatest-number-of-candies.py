class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_list=[]
        for candy in candies:
            new_list.append((candy + extraCandies) >= max(candies))  
        return new_list