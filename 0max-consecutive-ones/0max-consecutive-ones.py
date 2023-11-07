class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_one = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                count +=1
                max_one = max(max_one, count)
            if nums[i] == 0:
                count = 0
                max_one = max(max_one, count)
        return max_one
            