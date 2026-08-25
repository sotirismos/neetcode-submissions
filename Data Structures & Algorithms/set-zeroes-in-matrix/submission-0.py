class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = {'rows': [], 'cols': []}
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                if matrix[row_index][col_index] == 0:
                    zeroes['rows'].append(row_index)
                    zeroes['cols'].append(col_index)
        
        for row_index, row in enumerate(matrix):
            if row_index in zeroes['rows']:
                for col_index, col in enumerate(row):
                    matrix[row_index][col_index] = 0
            else:
                for col_index, col in enumerate(row):
                    if col_index in zeroes['cols']:
                        matrix[row_index][col_index] = 0
        