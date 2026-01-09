class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        window= 0
        for num in nums:
            if num == 1:
                window +=1 
            else:
                window = 0
            max_one = max(max_one, window)
        return max_one