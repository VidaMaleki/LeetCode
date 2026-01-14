class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left1, right1 = 0, len(nums)
        while left1 < right1:
            mid = (left1 + right1) // 2
            if nums[mid] < target:
                left1 = mid + 1
            else:
                right1 = mid
        
        left2, right2 = 0, len(nums)
        while left2 < right2:
            mid = (left2 + right2) // 2
            if nums[mid] <= target:
                left2 = mid + 1
            else:
                right2 = mid
            
        start = left1
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = left2 -1
        return [start, end]
