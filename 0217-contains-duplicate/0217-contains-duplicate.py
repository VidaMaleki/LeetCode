class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) != len(nums):
            return True
        return False
            