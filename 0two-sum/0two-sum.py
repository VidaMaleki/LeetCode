class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left= 0
        right = 1
        while left < len(nums):
            if nums[left] + nums[right] == target:
                return [left, right]
            if right == len(nums) -1:
                right = left +1
                left +=1
            right +=1
        