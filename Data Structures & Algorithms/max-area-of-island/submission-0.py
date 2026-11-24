class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_path = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r: int, c: int) -> int:
            # Base case (out of bounds, visited or invalid cell)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            # Choose
            grid[r][c] = 0
            current_path = 1

            # Explore
            for dr, dc in neighbors:
                current_path += dfs(r + dr, c + dc)
            
            return current_path

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    current_path = dfs(r, c)
                    max_path = max(max_path, current_path)
        
        return max_path
