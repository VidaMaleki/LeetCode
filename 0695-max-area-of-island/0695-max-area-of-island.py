class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        def dfs(row, col):
            if (row < 0 or row >= rows or
                col < 0 or col >= columns or grid[row][col] == 0 or (row, col) in seen):
                return 0
            seen.add((row, col))
            size = 1
            size += dfs(row+1, col)
            size += dfs(row-1, col)
            size += dfs(row, col+1)
            size += dfs(row, col-1)
            return size
        
        max_island = 0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1 and (row, col) not in seen:
                    current_island = dfs(row, col)
                    max_island = max(max_island, current_island)
        return max_island