class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 1), (1, 0), (0, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]
        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (rows -1, cols -1):
                return steps
            for r, c in directions:
                new_row, new_col = row + r, col + c
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps+1))
        return -1