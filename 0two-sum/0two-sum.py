class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums_dict:
                return [nums_dict[pair], i]
            nums_dict[num] = i
        return []