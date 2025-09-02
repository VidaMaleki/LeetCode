from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        return max(nums_dict, key=nums_dict.get)