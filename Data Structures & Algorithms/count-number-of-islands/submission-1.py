class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int):       
            # Base case (out of bounds or land)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return 
            # Choose (add node to path)
            grid[r][c] = "0"
            # Explore
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # New island detected
                    dfs(r, c)
                    islands += 1
        
        return islands