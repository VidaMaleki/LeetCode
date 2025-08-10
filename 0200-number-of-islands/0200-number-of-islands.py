from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        count = 0
        def dfs(row, col):
            if (row < 0 or row >= rows or
                col < 0 or col >= columns or grid[row][col] == "0" or (row, col) in seen):
                return
            seen.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    count +=1
        return count