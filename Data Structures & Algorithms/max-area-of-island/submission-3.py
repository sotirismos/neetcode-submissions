class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_path = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int) -> int:
            # Base case (out of bounds, visited or invalid cell)
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == 0:
                return 0

            # Choose
            visit.add((r, c))
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    current_path = dfs(r, c)
                    max_path = max(max_path, current_path)
        
        return max_path
