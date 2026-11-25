class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visit, previous_height):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r >= num_rows or c >= num_cols or
                heights[r][c] < previous_height):
                    return 

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for row in range(num_rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, num_cols - 1, atlantic, heights[row][num_cols - 1])
        
        for col in range(num_cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(num_rows - 1, col, atlantic, heights[num_rows - 1][col])

        res = []
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res
        


