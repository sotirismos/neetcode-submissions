class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r: int, c: int):
            # Base case (out of bounds or invalid cell)
            if (r < 0 or c < 0 or r >= num_rows or c >= num_cols or board[r][c] != "O"):
                return
            
            # Mark as safe
            board[r][c] = "S"
            
            # Explore
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(num_rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][num_cols - 1] == "O":
                dfs(r, num_cols - 1)
        
        for c in range(num_cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[num_rows - 1][c] == "O":
                dfs(num_rows - 1, c)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
