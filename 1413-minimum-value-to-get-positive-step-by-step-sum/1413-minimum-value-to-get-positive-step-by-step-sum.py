class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        left = 0
        window_sum = 0
        
        while left < len(nums):
            window_sum += nums[left]
            temp = start + window_sum
            
            while temp < 1:
                start +=1
                temp = start + window_sum
            
            left +=1
        return start