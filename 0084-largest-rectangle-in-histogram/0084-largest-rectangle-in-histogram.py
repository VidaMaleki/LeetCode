class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            # close rectangles that are too tall
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx

            stack.append((start, h))

        # any bars left
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))

        return max_area

    