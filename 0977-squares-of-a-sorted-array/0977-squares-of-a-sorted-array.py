class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = len(nums)-1
        left = 0
        size = len(nums)-1
        new_list = [0] * len(nums)
        while left<= right:
            temp1 = nums[left] * nums[left]
            temp2 = nums[right] * nums[right]
            if temp1 > temp2:
                new_list[size] = temp1
                left +=1
                size -=1
            else:
                new_list[size] =temp2
                right -=1
                size -=1
        return new_list