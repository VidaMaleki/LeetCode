class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i]+ current_sum)
            max_sum = max(max_sum, current_sum)
        return max_sum 
                
        