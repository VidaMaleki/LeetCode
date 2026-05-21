class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        for i in range(k, len(nums)):
            print(nums[i])
            window_sum -= nums[left]
            window_sum += nums[i]
            max_avg = max(max_avg, window_sum / k)
            left+=1
        return max_avg