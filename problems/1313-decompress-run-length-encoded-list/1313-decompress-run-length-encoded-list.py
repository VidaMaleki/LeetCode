class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_list = []
        for val in range(1, len(nums), 2):
            freq = nums[val-1]
            new_list += [nums[val]] * freq  
        return new_list