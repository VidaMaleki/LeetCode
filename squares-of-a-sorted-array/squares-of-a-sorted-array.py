class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = []
        for num in nums:
            square = num * num
            square_list.append(square)
        return sorted(square_list)