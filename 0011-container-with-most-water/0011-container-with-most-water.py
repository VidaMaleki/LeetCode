class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) -1
        left = 0
        ans = 0
        while left< right:
            diff = right - left
            if height[left] < height[right]:
                water = diff * height[left]
                left +=1
            else:
                water = diff * height[right]
                right -= 1
            ans = max(water , ans)
        return ans
