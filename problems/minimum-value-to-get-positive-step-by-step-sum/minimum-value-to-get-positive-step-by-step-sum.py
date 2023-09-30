class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum_nums = [nums[0]]
        for i in range(1, len(nums)):
            sum_nums.append(nums[i] +sum_nums[-1])
        
        min_num = min(sum_nums)
        if min_num > 0:
            return 1
        
        return abs(min_num) + 1