class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path_so_far = set()

        def backtracking(row_index: int, col_index: int, path_so_far: set, current_index: int) -> bool:
            # Base case (reached word)
            if current_index == len(word):
                return True
            # Base case (out of bounds)
            if (row_index < 0) or (row_index > len(board) - 1) or (col_index < 0) or (col_index > len(board[row_index]) - 1):
                return False
            # Base case (character mismatch)
            if word[current_index] != board[row_index][col_index]:
                return False
            
            # add char to the path
            path_so_far.add((row_index, col_index))

            # explore up
            if (row_index - 1, col_index) not in path_so_far:
                if backtracking(row_index - 1, col_index, path_so_far, current_index + 1):
                    return True
            # explore down
            if (row_index + 1, col_index) not in path_so_far:
                if backtracking(row_index + 1, col_index, path_so_far, current_index + 1):
                    return True
            # explore right
            if (row_index, col_index + 1) not in path_so_far:
                if backtracking(row_index, col_index + 1, path_so_far, current_index + 1):
                    return True
            # explore left
            if (row_index, col_index - 1) not in path_so_far:
                if backtracking(row_index, col_index - 1, path_so_far, current_index + 1):
                    return True

            # backtrack
            path_so_far.remove((row_index, col_index))
            return False
        

        for row_index, row in enumerate(board):
            for col_index, col in enumerate(board[row_index]):
                if backtracking(row_index, col_index, path_so_far, 0):
                    return True
        return False