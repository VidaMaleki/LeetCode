class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]= [nums[(i - k) % len(nums)]for i, x in enumerate(nums)]
        return nums