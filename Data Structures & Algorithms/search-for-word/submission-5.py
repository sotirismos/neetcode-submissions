class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(board[row_index]):
                current_path = set()
                if self.helper(board, word, row_index, col_index, current_path, 0):
                    return True
        return False


    def helper(self, board: List[List[str]], word: str, row_index: int, col_index: int, current_path: set, index: int) -> bool:
        # Row out of bounds
        if row_index >= len(board) or row_index < 0:
            return False
        # Col out of bounds
        if col_index >= len(board[row_index]) or col_index < 0:
            return False
        # Cell differs from word[i]
        if board[row_index][col_index] != word[index]:
            return False
        # We just matched the last letter
        if index == len(word) - 1:
            return True
        
        # Track the path
        current_path.add((row_index, col_index))

        if (row_index, col_index + 1) not in current_path:
            if self.helper(board, word, row_index, col_index + 1, current_path, index + 1):
                return True

        if (row_index + 1, col_index) not in current_path:
            if self.helper(board, word, row_index + 1, col_index, current_path, index + 1):
                return True

        if (row_index, col_index - 1) not in current_path:
            if self.helper(board, word, row_index, col_index - 1, current_path, index + 1):
                return True

        if (row_index - 1, col_index) not in current_path:
            if self.helper(board, word, row_index - 1, col_index, current_path, index + 1):
                return True
        
        current_path.remove((row_index, col_index))
        
