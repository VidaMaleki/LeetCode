class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums