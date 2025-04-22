class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if nums[0] >= target:
            return 1
        nums_sum = nums[0]
        ans = float("inf")
        left = 0
        for i in range(1, len(nums)):
            nums_sum += nums[i]       
            while nums_sum >= target:
                ans = min(ans, i - left + 1)
                nums_sum -= nums[left]
                left +=1
        return ans