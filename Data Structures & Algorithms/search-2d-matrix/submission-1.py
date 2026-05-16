class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row:List[int], target):
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] > target:
                    right = mid - 1
                elif row[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False
        
        for row in matrix:
            if binary_search(row, target):
                return True
        
        return False