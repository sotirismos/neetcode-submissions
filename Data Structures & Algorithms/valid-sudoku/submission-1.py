class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = {} 
        col_dict = {}
        box_dict = {}

        for row_index, row in enumerate(board):
            for col_index, val in enumerate(row):
                # Row
                if val == '.':
                    continue
                if row_index not in row_dict:
                    row_dict[row_index] = set()
                if row_index in row_dict:
                    if val in row_dict[row_index]:
                        return False
                    else:
                        row_dict[row_index].add(val)

                # Column
                if col_index not in col_dict:
                    col_dict[col_index] = set()
                if col_index in col_dict:
                    if val in col_dict[col_index]:
                        return False
                    else:
                        col_dict[col_index].add(val)

                # Box
                box_index = (row_index // 3, col_index // 3)
                if box_index not in box_dict:
                    box_dict[box_index] = set()
                if box_index in box_dict:
                    if val in box_dict[box_index]:
                        return False
                    else:
                        box_dict[box_index].add(val)
        return True