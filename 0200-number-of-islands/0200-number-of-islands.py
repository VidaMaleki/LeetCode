class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def explore(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            explore(i +1, j)
            explore(i -1, j)
            explore(i , j + 1)
            explore(i, j -1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count +=1
                    explore(i, j)
        return count

        
