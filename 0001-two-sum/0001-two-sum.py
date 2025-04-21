class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in checked_nums:
                return [checked_nums[pair], i]
            else:
                checked_nums[num] = i
        