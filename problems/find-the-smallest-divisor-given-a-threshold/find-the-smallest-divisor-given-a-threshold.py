import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Input: nums = [1,2,5,9], threshold = 6
        # Output: 5
        nums.sort()
        left = 1
        right = max(nums) # 3
        while left <= right:
            mid = (left + right) // 2 # 1
            total = 0
            for num in nums:
                total += math.ceil(num / mid) # 
            if total > threshold:
                left = mid +1
            else: 
                right = mid -1
        return left