class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return nums
        left =0
        for num in nums:
            if num != 0:
                nums[left] = num
                left+=1
        
        nums[left:] = [0]* (len(nums) -left)

        