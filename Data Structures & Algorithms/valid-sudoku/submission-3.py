class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)

        # Traverse each column
        for row_index, row in enumerate(board):
            # Traverse each row
            for col_index, col in enumerate(board[row_index]):
                # Skip '.'
                if board[row_index][col_index] == '.':
                    continue
                # Check the row
                if board[row_index][col_index] in row_dict[row_index]:
                    return False
                else:
                    row_dict[row_index].add(board[row_index][col_index])
                
                # Check the column
                if board[row_index][col_index] in col_dict[col_index]:
                    return False
                else:
                    col_dict[col_index].add(board[row_index][col_index])
                
                # Check the box
                current_box = (row_index // 3, col_index // 3)
                if board[row_index][col_index] in box_dict[current_box]:
                    return False
                else:
                    box_dict[current_box].add(board[row_index][col_index])
    
        return True

                           

