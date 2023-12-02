class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = left +1
        while left != len(nums)-1:
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left +=1
                right +=1
        return len(nums)