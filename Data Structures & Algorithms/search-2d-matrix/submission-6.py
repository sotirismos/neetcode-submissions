class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                break

        left_row = 0
        right_row = len(matrix[mid]) - 1

        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2

            if target > matrix[mid][mid_row]:
                left_row = mid_row + 1
            elif target < matrix[mid][mid_row]:
                right_row = mid_row - 1
            else:
                return True
        
        return False