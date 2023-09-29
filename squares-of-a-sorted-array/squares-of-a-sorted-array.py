class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_list = []
        left = 0
        right = len(nums)-1
        while left < right:
            max_right = nums[right] * nums[right] 
            max_left = nums[left] * nums[left]
            if (max_right) > (max_left):
                squared_list.insert(0,max_right)
                right -= 1
            else:
                squared_list.insert(0,max_left)
                left += 1
        print("left", left, "right", right)
        
        temp = nums[left] * nums[left]
        squared_list.insert(0, temp)
        
        return squared_list