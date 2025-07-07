class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [i, nums_dict[diff]]
            nums_dict[num] = i
        

        