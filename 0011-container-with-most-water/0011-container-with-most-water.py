class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the width and height of the container
            width = right - left
            container_height = min(height[left], height[right])

            # Update the maximum area if the current area is greater
            max_area = max(max_area, width * container_height)

            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area