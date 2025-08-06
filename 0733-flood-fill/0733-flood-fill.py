class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, columns = len(image), len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(row, col):
            if (row < 0 or row >= rows or col < 0 or col >= columns or image[row][col] != original_color):
                return
            image[row][col] = color
            dfs(row -1, col)
            dfs(row +1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        dfs(sr, sc)
        return image
