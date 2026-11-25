class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        starting_pixel_color = image[sr][sc]

        def dfs(r: int, c: int):
            # Base case (pixel is out of bounds)
            if r < 0 or c < 0 or r >= num_rows or c >= num_cols:
                return
            # Base case (pixel does not have the same color as the starting pixel)
            if image[r][c] != starting_pixel_color:
                return
            # Base case (already visited (& painted) pixel)
            if image[r][c] == color:
                return
            
            # paint pixel
            image[r][c] = color

            # explore neighbors
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        dfs(sr, sc)

        return image
