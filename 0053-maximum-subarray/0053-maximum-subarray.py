class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        window_sum = nums[0] 
        max_sub = nums[0] 
        for i in range(1,len(nums)):
            window_sum = max(nums[i], window_sum+nums[i])
            max_sub = max(window_sum,max_sub )
        return max_sub
