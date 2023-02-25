class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        ans = 0
        current = 1
        for i in range(len(nums)):
            current *= nums[i]
            while current >= k:
                current //= nums[left]
                left +=1
            ans += i - left + 1
        return ans